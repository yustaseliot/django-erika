from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name="post_detail"),
    url(r'', include('django.contrib.flatpages.urls')),
]
