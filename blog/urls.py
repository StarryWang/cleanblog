from django.conf.urls import url
from . import views

app_name = '[blog]'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.page_detail, name='page_detail'),
    url(r'^about$', views.about, name='about'),
    url(r'^sub_index$', views.sub_index, name='sub'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^blog_index', views.blogs, name='blog_index'),
    url(r'^post_shar', views.post_share, name='post_share'),
    url(r'^edit/(?P<blog_id>[0-9]+)/$', views.edit, name='edit'),

]
