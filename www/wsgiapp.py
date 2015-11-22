#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A WSGI application entry.
'''

import logging; logging.basicConfig(level=logging.INFO)

import os, time, datetime

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

import urls

# www files directory
www_dir = os.path.dirname(os.path.abspath(__file__))

# datetime filter
def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)

    dt = datetime.datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

# template engine
tmpl_engine = Jinja2TemplateEngine(os.path.join(www_dir, 'templates'))
tmpl_engine.add_filter('datetime', datetime_filter)

# init db:
db.create_engine(**configs.db)

# init wsgi app:
wsgi = WSGIApplication(www_dir)
wsgi.template_engine = tmpl_engine
wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(9000)
# else:
#   application = wsgi.get_wsgi_application()
