from alert.models import Category, UserProfile, Report, UserReport
from geopy.geocoders import Nominatim


def category_count(user):
    """

    :param user:
    :return: category count for each keyword
    """
    temp = list()

    categories = Category.objects.all()
    userprofile = UserProfile.objects.get(user=user)

    for category in categories:
        reports = len(UserReport.objects.filter(
            userprofile=userprofile, report__category__name=category.name))

        temp.append(reports)

    return temp


def category_percent(user):
    """

    :param user:
    :return: percentage of each category
    """
    temp = category_count(user)
    total = sum(temp)
    percent = list()
    context = dict()

    for item in temp:
        if total != 0:
            percent.append((item / total) * 100)

    categories = Category.objects.all()

    for category, p in zip(categories, percent):
        context[category.name] = round(p, 2)

    return context


def get_location(place):
    geolocator = Nominatim(user_agent="my_user_agent")
    loc = geolocator.geocode(place)
    return loc.latitude, loc.longitude
