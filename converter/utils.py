import new
from converter.models import Database

def get_source_list():
    return tuple(Database.objects.filter(active = 1).order_by('name').values_list('id', 'name'))

def get_database_list(_id):
    source = Database.objects.get(id = _id)
    _module = new.module('db_connection')
    exec str(source.code) in _module.__dict__
    if _module.DB_LIST_QUERY:
        cursor = _module.get_connection(source.db_name, source.location, source.username, source.password)
        cursor.execute(_module.DB_LIST_QUERY)
        db_list = [e_value(x) for x in cursor.fetchall()]
    else:
        db_list = [source.db_name]
    return tuple(zip(db_list, db_list))

def get_table_list(_id, db_name):
    source = Database.objects.get(id = _id)
    _module = new.module('db_connection')
    exec str(source.code) in _module.__dict__
    cursor = _module.get_connection(db_name, source.location, source.username, source.password)
    try:
        _table_query = _module.TABLE_LIST_QUERY %(db_name)
    except TypeError, e:
        _table_query = _module.TABLE_LIST_QUERY
    cursor.execute(_table_query)
    table_list = [e_value(x) for x in cursor.fetchall()]
    return tuple(zip(table_list, table_list))

def get_data(_id, db_name, query):
    source = Database.objects.get(id = _id)
    _module = new.module('db_connection')
    exec str(source.code) in _module.__dict__
    cursor = _module.get_connection(db_name, source.location, source.username, source.password)
    cursor.execute(query)
    return cursor.fetchall()
   
e_value = lambda x : x.values()[0] if isinstance(x,(dict)) else x[0]

def transform_to_triple(source, db_name, table, result):
    #get the list of relations for the selected DB
    max_records = 100
    response = []
    x_print = lambda *x : response.append("<tr>%s</tr>" %("".join(["<td>%s</td>"%(v) for v in x])))
    id = 1
    x_print("Subject", "Predicate", "Object")
    x_print(id,'dbname:string',db_name)
    tables = []
    table_list = [table,]
    for i, _table in enumerate(table_list):
        _table_id = id + i + 1
        x_print(id,'rel:id', _table_id)
        _schema = "SELECT column_name,column_type FROM information_schema.columns WHERE table_schema = '%s' \
                   AND table_name='%s' ORDER BY ordinal_position;" %(db_name, _table)
        #tuple having first value as table name and second for column description
        tables.append((_table_id, _table, get_data(source, db_name, _schema)))
    for _table in tables:
        _table_id = _table[0]
        x_print(_table_id,'rel_name:string',_table[1])
        for j,row in enumerate(result):
            #lets assume there is always less than 10 k tuples in a table
            _tuple_id = _table_id * max_records + j + 1
            x_print(_table[0],'tuple:id', _tuple_id)
        for j,row in enumerate(result):
            _tuple_id = _table_id * max_records + j + 1
            for k,value in enumerate(row):
                x_print(_tuple_id, "%s : %s" %(_table[2][k][0], _table[2][k][1]), value)
    return "<table border=\"1\">%s</table>" %("".join(response))
