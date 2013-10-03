from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'apps.account.views',
    url(r'^$',         'status_view'),
    url(r'^login$',    'login_view'),
    url(r'^logout$',   'logout_view'),
    url(r'^register$', 'register_view'),
    url(r'^bind$',     'bind_view'),
)
