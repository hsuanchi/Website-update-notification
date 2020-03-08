from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint
from .. import db

editcrawler = Blueprint('editcrawler', __name__)


def get_is_admin():
    return session.get('role')


@editcrawler.route('/add', methods=['POST'])
def add():
    if get_is_admin() == 'Y':
        data = request.json
        sql = f'INSERT INTO websiteStructureList(website_name, css_name, css_description, css_link, website_url, status) VALUES ("{data["website"]}", "{data["name"]}", "{data["description"]}","{data["link"]}","{data["url"]}", "Y")'
        db.engine.execute(sql)
        response = jsonify({'msg': 'ok'})
    else:
        response = jsonify({'msg': '權限不足'})
    return response


@editcrawler.route('/delete', methods=['POST'])
def deleteproduct():
    if get_is_admin() == 'Y':

        data = request.json
        sql = f"update websiteStructureList set status = 'N' where wid = {data['wid']} "
        db.engine.execute(sql)
        response = jsonify({'msg': 'ok'})
    else:
        response = jsonify({'msg': '權限不足'})
    return response


@editcrawler.route('/updata', methods=['POST'])
def updataproduct():
    if get_is_admin() == 'Y':

        data = request.json
        sql = f'update websiteStructureList set website_name = "{data["website"]}", css_name = "{data["name"]}", css_description = "{data["description"]}", css_link = "{data["link"]}", website_url = "{data["website_url"]}" where wid = {data["id"]} '
        db.engine.execute(sql)

        response = jsonify({'msg': 'ok'})
    else:
        response = jsonify({'msg': '權限不足'})
    return response
