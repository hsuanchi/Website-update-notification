from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint
from .. import db
from .crawler import Main

status = Blueprint('status', __name__)


def get_is_admin():
    return session.get('role')


@status.route('/restart', methods=['POST'])
def restart():
    if get_is_admin() == 'Y':

        data = request.json
        if data['id'] == 'All':
            obj_Crawler = Main.Crawler()
            obj_Crawler.crawl(db, 'All')
            status = 'ok'
        else:
            obj_Crawler = Main.Crawler()
            obj_Crawler.crawl(db, data['id'])
            status = 'ok'
    else:
        status = '權限不足'

    response = jsonify({
        'msg': status
    })

    return response
