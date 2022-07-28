from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "EH"
password = "123"
facebook_friends=["Yuval","Omar","Guy", "Maor", "Yair", "jon jonny", "jack the dull boy", "ysdarehet dude"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		word = request.form['password']
		if name == username and word == password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', frens=facebook_friends)


@app.route('/friend_exists/<string:friend>', methods=['GET', 'POST'])
def friend_exists(friend):
	if friend in facebook_friends:
		return render_template('friend_exists.html', friend=friend, is_friend=True)
	else:
		return render_template('friend_exists.html', friend=friend, is_friend=False)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)