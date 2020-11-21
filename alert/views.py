from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from alert.models import UserProfile, Notifications, Category, Report, UserReport, Keyword
from scheduler.models import ScrapedLink
from django.contrib import messages
from django.http import JsonResponse
from utils.social import social_media_scrape, send_alerts
from utils.analytics import category_percent, get_location, category_count
import json, copy, random


def index(request):
    context_dict = dict()

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')
    unread = notifications.filter(read=False)
    user_crawled_links = UserReport.objects.filter(userprofile=userprofile).order_by('-pub_date')

    context_dict['home'] = True
    context_dict['userprofile'] = userprofile
    context_dict['unread_count'] = len(unread)
    context_dict['notifications'] = notifications[:5]
    context_dict['category'] = category
    context_dict['user_crawler'] = user_crawled_links[:userprofile.recent_link]
    context_dict['cat_percent'] = category_percent(request.user)
    return render(request, 'alert/index.html', context=context_dict)

@login_required
def map(request):
    context_dict = dict()

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')
    unread = notifications.filter(read=False)

    context_dict['map'] = True
    context_dict['userprofile'] = userprofile
    context_dict['unread_count'] = len(unread)
    context_dict['notifications'] = notifications[:5]
    context_dict['category'] = category
    return render(request, 'alert/map.html', context=context_dict)


@login_required
def reports(request):
    """

    :param request:
    :return: Crawler Page
    """
    context = dict()
    userprofile = UserProfile.objects.get(user=request.user)
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')
    unread = notifications.filter(read=False)
    categories = [i.name for i in Category.objects.all()]
    user_reports = UserReport.objects.order_by('-pub_date')

    unique_keyword = list(user_reports.filter(userprofile=userprofile).order_by().values_list('report__keyword__name',
                                                                                              flat=True).distinct())

    copy_keyword = copy.copy(unique_keyword)
    random.shuffle(copy_keyword)

    print(category_count(request.user))
    context['report'] = True
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)
    context['user_reports'] = user_reports
    context['categories'] = categories
    context['category_data'] = category_count(request.user)
    context['unique_keyword'] = unique_keyword

    return render(request, "alert/report.html", context=context)


@login_required
def update(request):
    """

    :param request:
    :return: update profile settings
    """
    if request.method == 'POST':
        userprofile = UserProfile.objects.get(user=request.user)
        query = str(request.POST['query'])
        userprofile.concurrency = int(query)
        update_percent = (userprofile.concurrency / 10) * 100
        userprofile.save()

        content = "Concurrency updated successfully."
        notification = Notifications(user=userprofile, content=content)
        notification.save()

        messages.success(request, content, extra_tags='concurrent_update')
        new_notification = Notifications.objects.filter(user=userprofile, read=False)

        context = {
            'update': query,
            'update_percent': update_percent,
            'new_count': len(new_notification)
        }

        return render(request, 'alert/update.html', context=context)


@login_required
def update_notifications(request):
    """

    :param request:
    :return: generate report Notifications
    """
    if request.method == 'POST':
        userprofile = UserProfile.objects.get(user=request.user)
        keyword = str(request.POST['keyword'])
        alert = str(request.POST.get('alert', None))
        if alert:
            content = "Alert has been sent to nearest location"
        else:
            content = f"Report is being generated for '{keyword}'"
        notification = Notifications(user=userprofile, content=content)
        notification.save()

        return HttpResponse("1")


@login_required
def update_notifications_base(request):
    """

    :param request:
    :return: Notifications
    """
    if request.method == 'POST':
        userprofile = UserProfile.objects.get(user=request.user)
        notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

        context = {
            'notifications': notifications[:5]
        }

        return render(None, "alert/update_notifications.html", context=context)


@login_required
def read(request):
    """

    :param request:
    :return: Notifcations read/unread
    """
    if request.method == 'POST':
        userprofile = UserProfile.objects.get(user=request.user)
        notifications = Notifications.objects.filter(user=userprofile)

        for notification in notifications:
            notification.read = True
            notification.save()

        return HttpResponse("0")


def api(request, keyword):
    userprofile = UserProfile.objects.get(user=request.user)
    userreports = UserReport.objects.filter(userprofile=userprofile)
    coordinates = get_location(keyword)
    predicted_data = {
        'keyword': keyword,
        'coordinates': {
            'latitude': coordinates[0],
            'longitude': coordinates[1]
        },
        'Natural_Disaster': {
            'earthquake': '78%',
            'floods': '10%',
            'tsunami': '0%',
            'storms': '20%',
            'Accuracy score': '92 %',
            'News Authenticity': '95%',
        },
        'Crimes': {
            'murder': '21%',
            'kidnapping': '12%',
            'traffiking': '3%',
            'Accuracy score': '94%',
            'News Authenticity': '97%',
        },
        'Woman_Abuse': {
            'murder': '18%',
            'rape': '5%',
            'traffiking': '3%',
            'Accuracy score': '91%',
            'News Authenticity': '89%',
        },
        'Child_Abuse': {
            'murder': '21%',
            'kidnapping': '12%',
            'traffiking': '3%',
            'Accuracy score': '91%',
            'News Authenticity': '89%',
        }

    }

    return JsonResponse(predicted_data)


@login_required
def social(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        # key = Keyword.objects.get(name=keyword)
        # scrape_data = SocialMedia.objects.filter(keyword=key)
        scrape_data = social_media_scrape(keyword)
        context = {
            'scrape_data': scrape_data
        }
        return render(None, 'alert/social.html', context=context)


@login_required
def trigger_alert(request):
    if request.method == 'POST':
        status = request.POST.get('status', None)
        if status:
            send_alerts()
    return HttpResponse("success alerts")


@login_required
def process(request):
    """

    :param request:
    :return: Result Page
    """
    if request.method == 'POST':

        userprofile = UserProfile.objects.get(user=request.user)
        notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')
        unread = notifications.filter(read=False)

        main_search = request.POST.get('main_search')
        filters = request.POST['multiple_select']
        reschedule = request.POST.get('reschedule_crawler')
        print(main_search, filters, reschedule)
        filters_list = [x.strip(' ') for x in filters.split(',')]

        labels = ["earthquake", "tsunami", "storm", "floods"]
        no_of_links = 0

        keyword = Keyword.objects.get_or_create(name=main_search)[0]
        keyword.save()

        for cat in filters_list:
            category = Category.objects.get_or_create(name=cat)[0]
            category.save()

            coordinates = get_location(keyword.name)
            predicted_data = {
                'keyword': keyword.name,
                'coordinates': {
                    'latitude': coordinates[0],
                    'longitude': coordinates[1]
                },
                'Natural_Disaster': {
                    'earthquake': '78%',
                    'floods': '10%',
                    'tsunami': '0%',
                    'storms': '20%',
                    'Accuracy score': '92 %',
                    'News Authenticity': '95%',
                },
                'Crimes': {
                    'murder': '21%',
                    'kidnapping': '12%',
                    'traffiking': '3%',
                    'Accuracy score': '94%',
                    'News Authenticity': '97%',
                },
                'Woman_Abuse': {
                    'murder': '18%',
                    'rape': '5%',
                    'traffiking': '3%',
                    'Accuracy score': '91%',
                    'News Authenticity': '89%',
                },
                'Child_Abuse': {
                    'murder': '21%',
                    'kidnapping': '12%',
                    'traffiking': '3%',
                    'Accuracy score': '91%',
                    'News Authenticity': '89%',
                }

            }
            old_data = json.dumps(predicted_data)

            report = Report.objects.get_or_create(keyword=keyword, category=category, predicted_data=old_data)[0]
            report.save()

            user_report, created = UserReport.objects.get_or_create(userprofile=userprofile, report=report,
                                                                    reschedule=reschedule)
            user_report.save()

            scraped_link = ScrapedLink.objects.get_or_create(keyword=keyword.name, scrape_data=old_data,
                                                             schedule_day=reschedule)[0]
            scraped_link.save()

            if created:
                no_of_links += 1

            userprofile.crawled_links += no_of_links
            userprofile.save()

        context = dict()

        context['result'] = True
        context['userprofile'] = userprofile
        context['unread_count'] = len(unread)
        context['notifications'] = notifications[:5]
        context['query'] = main_search
        context['labels'] = labels

        return render(request, 'alert/result.html', context=context)
