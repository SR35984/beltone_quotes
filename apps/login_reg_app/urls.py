from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="landing"),
    url(r'^quotes$', views.quotes, name="dashboard"),
    url(r'^user/(?P<id>\d+)$', views.user, name="user"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
]