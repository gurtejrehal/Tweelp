from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink
# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)

from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink
# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)

from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink
# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)
from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink
# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)


from django.shortcuts import render, HttpResponse
from alert.models import UserProfile, Category, Notifications
from scheduler.models import ScrapedLink, RescrapedLink


# from scheduler.tasks import rescrape_one

def index(request):
    """
    :param request:
    :return:
    """

    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    category = Category.objects.all()
    notifications = Notifications.objects.filter(user=userprofile).order_by('-pub_date')

    unread = notifications.filter(read=False)

    scraped_links = ScrapedLink.objects.all()

    context = dict()
    context['scheduler'] = True
    context['category'] = category
    context['userprofile'] = userprofile
    context['notifications'] = notifications[:5]
    context['unread_count'] = len(unread)

    context['scraped_links'] = scraped_links

    return render(request, "scheduler/index.html", context=context)


def search(request):
    """
    :param request:
    :return:
    """
    empty = False
    if request.method == 'POST':
        search = request.POST.get('data')
        scrape_link = ScrapedLink.objects.get(keyword=search)
        try:
            rescrape_link = RescrapedLink.objects.get(keyword=scrape_link)
        except:
            empty = True
            rescrape_link = "Not Rescraped yet"

        context = {
            "scrape_link": scrape_link,
            "empty": empty,
            "rescrape_link": rescrape_link,
            "scheduler": True
        }

        return render(None, "scheduler/search.html", context=context)



