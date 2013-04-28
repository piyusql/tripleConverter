from django.conf.urls import patterns, include, url

urlpatterns = patterns('converter.views',
    # Examples:
    url(r'^structured', 'structured'),
    url(r'^semi-structured', 'semi_structured'),
    url(r'^un-structured', 'un_structured'),
)
