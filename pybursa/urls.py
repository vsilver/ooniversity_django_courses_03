from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import index, contact

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    # url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls'), name='quadratic'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),

    url(r'^admin/', include(admin.site.urls)),
)


