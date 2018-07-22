from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
url(r'^$',views.index,name="index"),
url(r'^search/$',views.search,name="search"),
url(r'^searchdate/$',views.searchdate,name="searchdate"),
url(r'^addfile/$',views.addfile,name="addfile"),

url(r'^delete-entry/(?P<pk>\d+)$', views.DeleteView, name='delete_view'),
#url(r'^add/$',views.add,name="add"),
]