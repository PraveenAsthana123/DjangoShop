from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^log_in/$', views.log_in, name="log_in"),
    url(r'^sign_up/$', views.sign_up, name="sign_up"),
    url(r'^welcome/$', views.welcome, name="welcome"),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout")
]
