from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from flask_login import login_user, logout_user, current_user
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
import datetime
blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/flask_blog')
def flask_blog():
    #구독 상태
    if current_user.is_authenticated:
        #구독 상태일시는 abTest가 진행되지 않게
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        #세션 저장
        BlogSession.save_session_info(session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email = current_user.user_email)
    #비구독 상태
    else:
        webpage_name = BlogSession.get_blog_page()
        #세션 저장
        BlogSession.save_session_info(session['client_id'], 'annoymous', webpage_name)
        #AB테스트를 위한 세션별 page
        return render_template(webpage_name)

#email 등록
@blog_abtest.route('/set_email', methods = ['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        return redirect(url_for('blog.flask_blog'))
    else:
        #content type이 application/json인 경우 request.form 사용
        #user 등록
        user = User.create(request.form['user_email'], request.form['blog_id'])
        #세션정보 등록, 로그인 유지
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        return redirect(url_for('blog.flask_blog'))
    
#구독취소
@blog_abtest.route('/logout')
def logout():
    #유저 삭제
    User.delete(current_user.id)
    #구독취소, 세션삭제
    logout_user()
    return redirect(url_for('blog.flask_blog'))
        