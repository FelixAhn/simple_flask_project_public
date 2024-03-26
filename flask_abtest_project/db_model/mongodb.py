import pymongo

#Mongodb 초기 설정
MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

#Mongodb 연결
def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        #blog_session_db에 있는 blog_ab 컬렉션 가지고 오기
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        #에러가 나면 다시 연결
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab
        