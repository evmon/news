from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from django.conf.urls import include

from .views import NewsView, NewsDetailView

app_name = "home_page"

urlpatterns = [

	url(r'^$', NewsView.as_view(), name='home'),
	url(r'^news/(?P<year>[-\w]+)/(?P<month>[-\w]+)/(?P<day>[-\w]+)/(?P<slug>[-\w]+)/$',
        NewsDetailView.as_view(),
		name='detail'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)