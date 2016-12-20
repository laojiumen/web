from django.conf.urls import url

from portal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(?P<god_id>.*)$', views.add_tag, name='add_tag')
]
