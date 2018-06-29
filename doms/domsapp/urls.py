from django.conf.urls import url,include
from . import views
urlpatterns=[
url(r'^$',views.index,name="index"),
url(r'^search/$',views.search,name="search"),
url(r'^addfile/$',views.addfile,name="addfile"),
#url(r'^add/$',views.add,name="add"),
]