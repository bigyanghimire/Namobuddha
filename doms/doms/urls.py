
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',include('domsapp.urls')),
    url(r'^files/',include('domsapp.urls')),
    
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)