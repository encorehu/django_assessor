from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from Assessor.api import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())
v1_api.register(ChoiceResource())
v1_api.register(QuizResource())
v1_api.register(UserResource())
v1_api.register(QuizQuestionResource())

admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
