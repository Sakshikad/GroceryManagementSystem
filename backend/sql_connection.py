import mysql.connector
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx == None:
        __cnx = mysql.connector.connect(user='root', password='9545373480',
                              host='127.0.0.1', database='grocery_store'
                              ,auth_plugin='mysql_native_password')
    return __cnx