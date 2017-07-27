from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from django.conf.urls import include

from .views import NewsView, page_view
# \, LoginView

app_name = "home_page"

urlpatterns = [
    url(r'^home/$', NewsView.as_view(), name=''),
    
    url(r'^', page_view, name='page_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)