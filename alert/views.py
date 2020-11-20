from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from alert.models import UserProfile, Notifications, Category
from django.contrib import messages


def index(request):
    context_dict = dict()

    userprofile = UserProfile.objects.get(user=request.user)
    category = Category.objects.all()
    context_dict['userprofile'] = userprofile
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
