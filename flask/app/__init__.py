# 引用flask套件
from flask import Flask, render_template, jsonify, request, session, redirect, make_response, url_for

# 引用sql相關模組
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# 引用time相關模組
import time
import datetime

# 引用其他相關模組
from .config.config import config
import pandas as pd
import requests

# MySql datebase
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # 設定config
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    @app.context_processor
    def check_login():
        check_auth = {
            'is_login': False,
            'is_admin': False,
            'user': None,
            'uid': None,
            'mode_type': None
        }
        try:
            check_auth['user'] = session.get('username')
            check_auth['uid'] = session.get('uid')
            check_auth['is_login'] = session.get('is_login')
            check_auth['is_admin'] = session.get('role')
            check_auth['mode_type'] = request.cookies.get('mode_type')
            return dict(check_auth=check_auth)
        except:
            return dict(check_auth=check_auth)

    @app.route('/')
    def index():

        return redirect(url_for('category.category_artical', get_tid='1'))

    @app.route('/admin')
    def page_list():
        sql_cmd = """
        SELECT tid,wid,crawler_name,crawler_description,crawler_link,ANY_VALUE(insert_time),TIMESTAMPDIFF(DAY,ANY_VALUE(insert_time),now()),website_name,website_url,tag
        FROM crawlerData NATURAL JOIN websiteStructureList
        group by tid,wid,crawler_name,crawler_description,crawler_link
        order by ANY_VALUE(insert_time) DESC
        """
        crawler_data = db.engine.execute(sql_cmd)
        return render_template('admin_list.html', crawler_data=crawler_data)

    return app


def register_extensions(app):
    """Register extensions with the Flask application."""
    # 讓每個模板都能使用csrf_token
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    # MySql datebase
    db.init_app(app)


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    from .views.category import category
    from .views.admin import admin
    from .views.admin_auth import auth
    from .views.admin_editcrawler import editcrawler
    from .views.admin_status import status
    app.register_blueprint(category, url_prefix='/category')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(editcrawler, url_prefix='/crawler')
    app.register_blueprint(status, url_prefix='/status')


def register_errorhandlers(app):
    """Register error handlers with the Flask application."""
    def render_error(e):
        return render_template('errors/%s.html' % e.code, error=e), e.code

    for e in [
            requests.codes.INTERNAL_SERVER_ERROR,
            requests.codes.NOT_FOUND,
            requests.codes.UNAUTHORIZED,
    ]:
        app.errorhandler(e)(render_error)
