from transwarp.web import WSGIApplication, Jinja2TemplateEngine
import website
import os

engine = Jinja2TemplateEngine('./templates')
engine.add_filter('datetime', lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))

wsgi = WSGIApplication('.')
wsgi.add_module(website)
wsgi.template_engine = engine

if __name__ == '__main__':
	wsgi.run()
else:
	application = wsgi.get_wsgi_application()
