import mysql.connector
db_connection = None
def get_sql_connection():
    global db_connection
    if db_connection is None:
        db_connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='gsjyothi')
    return db_connection