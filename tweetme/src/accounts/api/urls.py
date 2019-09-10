from django.conf.urls import url
from tweets.api.views import  TweetListAPIView
from django.views.generic.base import RedirectView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
	# url(r'^$', RedirectView.as_view(url="/")),
	url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'),

 ]

