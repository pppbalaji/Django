from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	(r'^articles/',include('article.urls')),
	url(r'^hello/','article.views.hello'),
	url(r'^hello_template/','article.views.hello_template'),
	url(r'^check/','article.views.check'),

    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^profileform/','django_test.views.show_profileform'),
	url(r'^thankyou/','django_test.views.thankyou'),
	
	
)
