from django.conf.urls import patterns, url
from views import search, search_form, TimeDetailView

urlpatterns = patterns('',
    url(r'^$', search_form, name='select'),
    url(r'^(?P<pk>[0-9]+)/$', TimeDetailView.as_view(), name='detail'),
    url(r'search/$', search, name='search')
)
