from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'test', views.login, name="login"),
    url(r'', views.logout, name="logout"),
]