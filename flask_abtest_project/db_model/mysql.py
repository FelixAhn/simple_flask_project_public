import pymysql

#mysql 초기설정
MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host= MYSQL_HOST,
    port = 3306,
    #자신의 mysql을 설정하세요(user, passwd)
    user = '',
    passwd= '',
    db = 'blog_db',
    charset= 'utf8'
)

#mysql 연결
def conn_mysqldb():
    #Mysql연결 끊겼을 시 재연결
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
