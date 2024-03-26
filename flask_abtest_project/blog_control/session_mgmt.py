from db_model.mongodb import conn_mongodb
from datetime import datetime

class BlogSession():
    blog_page = {'A' : 'blog_A.html', 'B' : 'blog_B.html'}
    session_count = 0
    
    #접속 기록
    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%Y.%m.%d %H:%M:%S")
        
        mong_db = conn_mongodb()
        mong_db.insert_one({
            'session_ip' : session_ip,
            'user_email' : user_email,
            'page' : webpage_name,
            'access_time' : now_time
        })
        
    @staticmethod
    def get_blog_page(blog_id=None):
        #abTest 관련
        if blog_id == None:
            if BlogSession.session_count == 0:
                BlogSession.session_count = 1
                return BlogSession.blog_page['A']
            else:
                BlogSession.session_count = 0
                return BlogSession.blog_page['B']
        else:
            return BlogSession.blog_page[blog_id]