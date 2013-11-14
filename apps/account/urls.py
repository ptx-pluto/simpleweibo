from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'account.views',
    url(r'^$',         'account_view'),
    url(r'^register$', 'register_view'),
)
