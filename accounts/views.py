from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.views import login as auth_login
from .models import Profile

def login(request):
    provider_list = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        provider_list.append(provider)

    return auth_login(request, authentication_form=LoginForm,
            extra_context={
                'provider_list': provider_list,
            })

def loginpage(request):
    return render(request, 'accounts/login.html')
