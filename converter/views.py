from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from converter.models import Database
from converter.utils import get_source_list, get_database_list, get_table_list,\
         get_data, transform_to_triple
from converter.ajax_methods import get_choice_data

@staff_member_required
def home(request):
    group_list = request.user.groups.all().values_list('name', flat = True)
    data = {'group_list' : group_list}
    return render_to_response('index.html', data, context_instance=RequestContext(request))

@staff_member_required
def structured(request):
    group_list = request.user.groups.all().values_list('name', flat = True)
    source_list = get_choice_data('Source', get_source_list())
    if request.POST:
        try:
            source = request.POST.get('source')
            db_name = request.POST.get('database')
            table_name = request.POST.get('table')
            query = request.POST.get('query')
            response = []
            if db_name:
                db_list = get_choice_data('DB', get_database_list(source))
                if table_name:
                    table_list = get_choice_data('Table', get_table_list(source, db_name))
                    query = "select * from %s limit 10;" %(table_name)
                    response = get_data(source, db_name, query)
                    triple_response = transform_to_triple(source, db_name, table_name, response)
        except Exception as e:
            response = "There is some error with the program for selected input please check\n\n%s" %(e)
        source = str(source)
    return render_to_response('converter/structured.html', locals(), context_instance=RequestContext(request))
 
@staff_member_required
def semi_structured(request):
    data = {}
    return render_to_response('not_available.html', data, context_instance=RequestContext(request))

@staff_member_required
def un_structured(request):
    data = {}
    return render_to_response('not_available.html', data, context_instance=RequestContext(request))
