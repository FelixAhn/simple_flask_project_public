from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
from blog_control.user_mgmt import User
import os

#https만 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

#서버 생성, html파일에서 가져올 데이터들은 static 폴더에서 가져올 수 있도록 설정
app = Flask(__name__, static_url_path='/static')
#추후 별도 서버간에 RestApi지원을 위해서 CORS 지원
CORS(app)
#flask 로그인과 관련(세션을 위해 고정된 값 설정)
app.secret_key = 'hong_server2'

#blue print등록
app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

login_manager = LoginManager()
#login_manager에 app등록
login_manager.init_app(app)
login_manager.session_protection = 'strong'

#user 로드
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

#login이 된 user만 접근가능하게
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

#클라이언트 세션 기록
@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)