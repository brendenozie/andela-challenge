from flask import render_template, request, json

from app import app

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/register')
def register():
	return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
        if request.method == 'POST':
		if valid_login(request.form['username'],request.form['password']):
            		return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
	return render_template('login.html', error=error)

@app.route('/account')
def account():
	return render_template("account.html")


@app.route('/registerUser', methods=['POST'])
def registerUser():
	if request.method =='POST':
		user =  request.form['username'];
    		password = request.form['password'];
		data={}
    		with open('file.txt', 'w') as f:
        		json.dump(data, f)
    		return render_template('account.html')
