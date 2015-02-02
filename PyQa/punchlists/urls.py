from django.conf.urls import patterns, url

from punchlists import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<punchlist_id>\d+)/$', views.issues, name='issues'),
	url(r'^(?P<punchlist_id>\d+)/reportissue/$', views.reportissue, name='reportissue'),
	url(r'^(?P<punchlist_id>\d+)/issue/review/(?P<issue_id>\d+)/$', views.set_issue_to_review, name='set_issue_to_review'),
	url(r'^(?P<punchlist_id>\d+)/issue/question/(?P<issue_id>\d+)/$', views.question_issue, name='question_issue'),
	url(r'^(?P<punchlist_id>\d+)/issue/complete/(?P<issue_id>\d+)/$', views.set_issue_as_complete, name='set_issue_as_complete'),
	url(r'^(?P<punchlist_id>\d+)/issue/notcomplete/(?P<issue_id>\d+)/$', views.set_issue_as_new, name='set_issue_as_new'),
)