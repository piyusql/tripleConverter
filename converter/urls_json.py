from django.conf.urls import patterns, include, url

urlpatterns = patterns('converter.ajax_methods',
    # Examples:
    url(r'^get_database_list', 'get_database_list'),
    url(r'^get_table_list', 'get_table_list'),
)
