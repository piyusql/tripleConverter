DB_LIST_QUERY = "show databases"
TABLE_LIST_QUERY = "select table_name from information_schema.tables where table_schema = '%s' and table_type = 'BASE TABLE';"
COLUMN_LIST_QUERY = ""

def get_connection(db, host, username, password):
    import MySQLdb
    conn = MySQLdb.connect(host = host, user = username, passwd = password, db = db)
    cur = conn.cursor()
    return cur
