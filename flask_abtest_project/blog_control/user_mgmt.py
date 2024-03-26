from flask_login import UserMixin
from db_model.mysql import conn_mysqldb

class User(UserMixin):
    #생성자
    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id
    
    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
        #연결된 db 가져오기
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        #sql문
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + str(user_id) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        #유저가 존재하지 않다면
        if not user:
            return None
        user = User(user_id = user[0], user_email=user[1], blog_id=user[2])
        return user
    
    @staticmethod
    def find(user_email):
        #연결된 db 가져오기
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        #sql문
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" + str(user_email) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        #유저가 존재하지 않다면
        if not user:
            return None
        user = User(user_id = user[0], user_email=user[1], blog_id=user[2])
        return user
    
    @staticmethod
    def create(user_email, blog_id):
        #우선 유저 조회
        user = User.find(user_email)
        #유저가 없다면 유저 생성
        if user == None:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            #sql문
            sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user
    
    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = 'DELETE FROM user_info WHERE USER_ID = %d' % (user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted