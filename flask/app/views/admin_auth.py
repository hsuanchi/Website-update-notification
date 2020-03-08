from flask import Flask, render_template, jsonify, request, session, redirect, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from ..model import sql
from .. import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        data = request.json
        password = data['password']
        query = sql.User.query.filter_by(email=data['email']).first()

        if query != None and check_password_hash(query.password, password):
            # 設置session
            session['username'] = query.email
            session['role'] = query.role
            session['uid'] = query.uid
            session['is_login'] = True
            session.permanent = True
            response = jsonify({
                'msg': 'ok'
            })
        else:
            response = jsonify({
                'msg': 'error'
            })
        return response


@auth.route('/logout', methods=['POST'])
def logout():
    # 設置session
    session['username'] = '未登入'
    session['role'] = None
    session['uid'] = None
    session['is_login'] = False

    response = jsonify({
        'msg': '登出'
    })
    return response


@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data['email']
    # 查詢
    query = sql.User.query.filter_by(email=email).first()
    if query == None:
        password = generate_password_hash(data['password'])
        # 新增使用者
        U = sql.User(email, password)
        db.session.add(U)
        db.session.commit()

        # 設置session
        query = sql.User.query.filter_by(email=email).first()
        session['username'] = query.email
        session['role'] = query.role
        session['uid'] = query.uid
        session['is_login'] = True
        session.permanent = True

        response = jsonify({
            'msg': '註冊成功'
        })
    else:
        response = jsonify({
            'msg': '重複註冊'
        })

    return response
