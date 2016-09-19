from flask import render_template
from app import app

@app.route('/')
def main():
	return 'Yup, This works'

@app.route('/index')
def index():
	user = {'nickname' : 'BlueTrainColtrane'}
	posts = [
		{
			'author' : {'nickname' : 'Mr. T'},
			'body' : 'You is a pity fool!'
		},
		{
			'author' : {'nickname' : 'Plant'},
			'body'	: 'Let me introduce to Led Zepellin'
		}
	]
	return render_template('index.html',title = 'Blog', user = user,
	 posts = posts)