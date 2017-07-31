from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from django.conf.urls import include

from .views import NewsView

app_name = "home_page"

urlpatterns = [
	
	url(r'^', NewsView.as_view(), name='home'),
	# url(r'^news/(?P<date>[-\w]+)/(?P<slug>[-\w]+)$', 
 	#        view.as_view(), name='Detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)