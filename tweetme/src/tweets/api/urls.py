from django.conf.urls import url
from .views import   LikeToggleAPIView, TweetListAPIView, TweetCreateAPIView, RetweetAPIView, TweetDetailAPIView
from django.views.generic.base import RedirectView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
	# url(r'^$', RedirectView.as_view(url="/")),
	url(r'^$', TweetListAPIView.as_view(), name='list'),
	url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
	url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
	# url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
	# url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view( ), name='update'),
	# url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
 ]

