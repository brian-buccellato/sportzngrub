from django.conf.urls import url
from django.conf.urls.static import static 
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^destinations/$', views.dest_list, name='dest_list'),
     url(r'^memories/$', views.memory_list, name='memory_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^page/$', views.page, name='edit_page'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
