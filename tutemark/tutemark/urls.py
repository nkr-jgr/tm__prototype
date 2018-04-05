from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from comingsoon.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutemark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^comingsoon/$', comingsoon_view),
	url(r'^about/$', about_view),
	#url(r'^comingsoon/contact/$', contact_view),
	url(r'^contact/$', contact_view),
	
	url(r'^comingsoon/feed_form/$', feedback_form_view),
	url(r'^about/feed_form/$', feedback_form_view),
	url(r'^comingsoon/feed_form/send_feedback_clean$', feedback_clean_view),
	url(r'^about/feed_form/send_feedback_clean$', feedback_clean_view),
	url(r'^comingsoon/feed_form/thanks/$', thank_view),
	url(r'^about/feed_form/thanks/$', thank_view),
    url(r'^admin/', include(admin.site.urls)),
)
