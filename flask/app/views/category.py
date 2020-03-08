from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Blueprint, make_response
from .. import db

category = Blueprint('category', __name__)


@category.route('/<string:get_tid>')
def category_artical(get_tid):
    mode = request.cookies.get('mode_type')
    # 取得 tid tag website_name
    sql_websiteStructureList = """
    select website_name,tag,tid,line_bot_url from websiteStructureList
    """
    data = db.engine.execute(sql_websiteStructureList)
    tag_attr = []
    website_tag_attr = []
    website_name_attr = []
    line_bot_url = []
    for i in data:
        if i.tag not in tag_attr:
            tag_attr.append(i.tag)
            website_tag_attr.append((i.tag, i.tid))
        if i.tid == get_tid and i.line_bot_url not in line_bot_url:
            line_bot_url.append(i.line_bot_url)
            pass
        if i.tid == get_tid:
            website_name_attr.append(i.website_name)
    # 取得文章清單
    sql_cmd = """
    SELECT tid,wid,crawler_name,crawler_description,crawler_link,ANY_VALUE(insert_time),TIMESTAMPDIFF(DAY,ANY_VALUE(insert_time),now()),website_name,website_url,tag
    FROM crawlerData NATURAL JOIN websiteStructureList
    where tid='{}'
    group by tid,wid,crawler_name,crawler_description,crawler_link
    order by ANY_VALUE(insert_time) DESC
    """.format(get_tid)

    crawler_data = db.engine.execute(sql_cmd)
    return render_template('category_artical.html', crawler_data=crawler_data, website_tag_attr=website_tag_attr, website_name_attr=website_name_attr, tid=get_tid, line_bot_url=line_bot_url[0], mode=mode)


@category.route('/<string:get_tid>/rss.xml')
def rss(get_tid):
    sql_cmd = """
    SELECT tid,wid,crawler_name,crawler_description,crawler_link,ANY_VALUE(insert_time),TIMESTAMPDIFF(DAY,ANY_VALUE(insert_time),now()),website_name,website_url,tag
    FROM crawlerData NATURAL JOIN websiteStructureList
    where tid='{}'
    group by tid,wid,crawler_name,crawler_description,crawler_link
    order by ANY_VALUE(insert_time) DESC
    """.format(get_tid)

    crawler_data = db.engine.execute(sql_cmd)
    template = render_template('rss.xml', data=crawler_data)
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response
