#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A WSGI application entry.
'''

import logging; logging.basicConfig(level=logging.INFO)

import os

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

import urls

# www files directory
www_dir = os.path.dirname(os.path.abspath(__file__))

# template engine
tmpl_engine = Jinja2TemplateEngine(os.path.join(www_dir, 'templates'))
# tmpl_engine.add_filter('datetime', lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))

# init db:
db.create_engine(**configs.db)

# init wsgi app:
wsgi = WSGIApplication(www_dir)
wsgi.template_engine = tmpl_engine
wsgi.add_module(urls)

if __name__ == '__main__':
	wsgi.run(9000)
# else:
#	application = wsgi.get_wsgi_application()
