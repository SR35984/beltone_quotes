from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="quotes_app_index"),
    url(r'^create$', views.create, name="create_quote"),
    url(r'^logout$', views.logout, name="logout"),
]
