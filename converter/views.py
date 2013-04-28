from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from converter.models import Database
from converter.forms import StructuredDataForm
from converter.utils import get_database_list, get_table_list, get_data


@staff_member_required
def home(request):
    group_list = request.user.groups.all().values_list('name', flat = True)
    print group_list
    data = {'group_list' : group_list}
    return render_to_response('index.html', data, context_instance=RequestContext(request))

@staff_member_required
def structured(request):
    group_list = request.user.groups.all().values_list('name', flat = True)
    data = {'group_list' : group_list}
    #import pdb;pdb.set_trace()
    form = StructuredDataForm()
    if request.POST:
        form = StructuredDataForm(request.POST)
        source = request.POST.get('source')
        db_name = request.POST.get('database')
        table_name = request.POST.get('table')
        query = request.POST.get('query')
        form.fields['database'].choices = get_database_list(source)
        if db_name:
            pass#form.fields['database'].initial = db_name
        if db_name:
            form.fields['table'].choices = get_table_list(source, db_name)
            if table_name:
                form.fields['table'].initial = table_name
        if table_name and not query:
            query = "select * from %s limit 10;" %(table_name)
        if query:
            form.fields['response'].initial = get_data(source, db_name, query)
    data['form'] = form
    return render_to_response('converter/structured.html', data, context_instance=RequestContext(request))

@staff_member_required
def semi_structured(request):
    data = {}
    return render_to_response('not_available.html', data, context_instance=RequestContext(request))

@staff_member_required
def un_structured(request):
    data = {}
    return render_to_response('not_available.html', data, context_instance=RequestContext(request))
