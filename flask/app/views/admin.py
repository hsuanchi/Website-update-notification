from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint
from .. import db

admin = Blueprint('admin', __name__)


@admin.route('/crawler')
def page_crawler():
    sql_cmd = "select * from websiteStructureList where status='Y'"
    crawler_data = db.engine.execute(sql_cmd)
    return render_template('admin_crawler.html', crawler_data=crawler_data)


@admin.route('/status')
def page_status():
    sql_cmd = """
    select wid,website_url,website_name,crawler_status,insert_time,TIMESTAMPDIFF(HOUR,insert_time,now())
    from (
        SELECT * 
        FROM statusLog a 
        WHERE insert_time = (
                            SELECT MAX(b.insert_time) 
                            FROM statusLog b 
                            WHERE a.wid = b.wid
                            )
        ) as table_log NATURAL JOIN websiteStructureList
    """
    crawler_statusLog = db.engine.execute(sql_cmd)
    return render_template('admin_status.html', crawler_statusLog=crawler_statusLog)
