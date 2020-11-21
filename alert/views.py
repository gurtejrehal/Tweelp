from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from alert.models import UserProfile, Notifications, Category
from django.contrib import messages
from utils.social import social_media_scrape, send_alerts


def index(request):
    context_dict = dict()

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')
    unread = notifications.filter(read=False)

    context_dict['home'] = True
    context_dict['userprofile'] = userprofile
    context_dict['unread_count'] = len(unread)
    context_dict['notifications'] = notifications[:5]
    context_dict['category'] = category
    return render(request, 'alert/index.html', context=context_dict)


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


def api(request):
    return HttpResponse("hey")


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
        reschedule_crawler = request.POST.get('reschedule_crawler')
        print(main_search, filters, reschedule_crawler)

        labels = ["earthquake", "tsunami", "storm", "floods"]
        context = dict()

        context['result'] = True
        context['userprofile'] = userprofile
        context['unread_count'] = len(unread)
        context['notifications'] = notifications[:5]
        context['query'] = main_search
        context['labels'] = labels

        return render(request, 'alert/result.html', context=context)
