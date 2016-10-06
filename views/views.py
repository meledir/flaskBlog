from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'nick': 'Meledir'}
  posts = [
  	{
  		'author': {'nick': 'Jack'},
  		'body': 'The film was great!'
  	},
  	{
		'author': {'nick': 'Rob'},
		'body': 'Beatiful day in France'  	
  	}
  ]
  return render_template('index.html', 
  	title = 'Home', 
  	user = user,
  	posts = posts)

@app.route('/hi')
@app.route('/hi/<name>')
def hi_world(name=None):
  return render_template('hello.html', name=name)

@app.route('/calc/sum/<int:arg1>/<int:arg2>')
def calc_sum(arg1, arg2):
  result = arg1 + arg2
  return 'Result = %d' % result