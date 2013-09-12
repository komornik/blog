from django.conf.urls.defaults import *
from mojprojekt.blog.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),

)