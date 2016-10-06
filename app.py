from flask import Flask 
app = Flask(__name__)


@app.route('/')
def index():
  return 'Index page here!'

@app.route('/hi')
def hi_world():
  return 'Hello, world!'

@app.route('/calc/sum/<int:arg1>/<int:arg2>')
def calc_sum(arg1, arg2):
  result = arg1 + arg2
  return 'Result = %d' % result
