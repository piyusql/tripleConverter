def hello(x):
    print "welcome %s !" %(x)
    print "following is the variables available : "
    print locals()
DB_LIST_QUERY = "show databases"
TABLE_LIST_QUERY = "select table_name from information_schema.tables where table_schema = '%s' and table_type = 'BASE TABLE';"
def get_connection(db, host, username, password):
    import MySQLdb
    conn = MySQLdb.connect(host = host, user = username, passwd = password, db = db)
    cur = conn.cursor()
    return cur

def execute_query(_cur, _sql):
    _cur.execute(_sql)
    print _cur.fetchall()
