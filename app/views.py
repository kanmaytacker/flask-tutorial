from flask import render_template
from app import app

@app.route('/')
def main():
	return 'Yup, This works'

@app.route('/index')
def index():
	user = {'nickname' : 'BlueTrainColtrane'}
	return render_template('index.html', title = 'Home', user = user)