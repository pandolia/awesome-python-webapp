from transwarp.web import view, get, interceptor, seeother, ctx
import datetime

@view('time.html')
@get('/')
def index():
	# return '<h1>Index page</h1>'
	return dict(name='Jack', posted_at=datetime.datetime.utcnow())

@get('/user/:id')
def show_user(id):
	# user = User.get(id)
	return 'Hello, %s' % id

@interceptor('/userq/')
def check_user_url(next):
	raise seeother('/user/iiid')
	# return next()

@get('/test')
def test():
	input_data = ctx.request.input()
	ctx.response.content_type = 'text/plain'
	ctx.response.set_cookie('name', 'value', expires=3600)
	return 'result'
