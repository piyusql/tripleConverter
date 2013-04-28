DB_LIST_QUERY = None
TABLE_LIST_QUERY = "SELECT * FROM sqlite_master where type='table'"

def get_connection(db, host, username, password):
    import sqlite3
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return cur
