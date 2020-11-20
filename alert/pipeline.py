from .models import UserProfile

# def save_profile_picture(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     url = None
#     profile = UserProfile.objects.get(user=user)
#     if backend.name == 'facebook':
#         url = "https://graph.facebook.com/%s/picture?type=large"%response['id']
#     if url:
#         profile.picture_url = url
#         profile.save()


def get_avatar(backend, strategy, details, response,
               user=None, *args, **kwargs):
    url = None
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
        profile = UserProfile.objects.get_or_create(user=user)[0]
        profile.picture_url = url
        profile.save()
