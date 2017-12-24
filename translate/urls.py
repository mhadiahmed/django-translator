from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
]
urlpatterns += patterns('',
 (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )
