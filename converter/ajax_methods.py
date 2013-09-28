from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from converter.utils import get_database_list as _get_database_list
from converter.utils import get_table_list as _get_table_list
 
def get_database_list( request ):
    source = request.REQUEST.get('source')
    db_list = [('','Please select DB')]
    db_list.extend(_get_database_list(source))
    return render_to_response( 'ajax_select_box.html', {'data': db_list}, context_instance = RequestContext(request))

def get_table_list( request ):
    source = request.REQUEST.get('source')
    db_name = request.REQUEST.get('database')
    table_list = [('','Please select Table')]
    table_list.extend(_get_table_list(source, db_name))
    return render_to_response( 'ajax_select_box.html', {'data': table_list}, context_instance = RequestContext(request))
