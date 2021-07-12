from flask import Flask, jsonify, session, request, redirect, url_for


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'2&YH3t45XxtnXkBho&vb@H8Wfbk$Z4*5'


@app.route('/')
def index():
	return jsonify({'ping': 'pong'})


@app.route('/hello')
def say_hello():
	if 'username' in session:
		result = {
			'status': 'successful',
			'message': f'Wazup {session["username"]}',
		}
		return jsonify(result)
	result = {
		'status': 'unsuccessful',
		'message': 'You are not logged in'
	}
	return jsonify(result)


@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.json['username']
		result = {
			'status': 'successful',
			'message': 'Logged in',
			'username': session['username'] 
		}
		return jsonify(result)
	result = {
		'status': 'unsuccessful',
		'message': 'Use the POST method'
	}
	return jsonify(result)


@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	result = {
		'status': 'successful',
		'message': 'Logged out.'
	}
	return jsonify(result)

