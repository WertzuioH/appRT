from django.conf.urls import url, include
from django.views.generic import ListView
from appRT.models import Post
from views import DisplayMovieView, index


urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("id"),template_name="appRT/list.html")),
	url(r'^top5', ListView.as_view(queryset=Post.objects.all().order_by("position")[:5],template_name="appRT/top5.html")),
	url(r'^details/(?P<position>\d+)/$', DisplayMovieView.as_view()),
	#url(r'^contact/', views.contact, name='contact'),
]