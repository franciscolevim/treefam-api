from flask import Flask, jsonify, session, request, redirect, url_for
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, login_user, logout_user, login_required

import json


app = Flask(__name__)
db = MongoEngine()
login_manager = LoginManager()
app.config['JSON_AS_ASCII'] = False
app.config['MONGODB_DB'] = 'family_tree'
app.config['MONGODB_HOST'] = 'mongodb_host'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'admintf'
app.config['MONGODB_PASSWORD'] = 'admin1234'
app.config['MONGODB_AUTH_SOURCE'] = 'admin'
app.secret_key = b'2&YH3t45XxtnXkBho&vb@H8Wfbk$Z4*5' # Set the secret key to some random bytes. Keep this really secret!
db.init_app(app)
login_manager.init_app(app)


@app.route('/')
def index():
	return jsonify({'ping': 'pong'})


@app.route('/hello')
@login_required
def say_hello():
	result = {
		'status': 'successful',
		'message': 'Wazup mafak'
	}
	return jsonify(result)


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()


@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username', 'guest')
	password = request.json.get('password', '')
	user = User.objects(name=username, password=password).first()
	if user:
		login_user(user)
		return jsonify(user.to_json())
	else:
		return jsonify({'status': 401, 'reason': 'Username or Password Error'})


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify(**{'result': 200, 'data': {'message': 'logout success'}})


class User(db.Document):

	name = db.StringField()
	password = db.StringField()
	email = db.StringField()


	def to_json(self):
		return {'name': self.name, 'email': self.email}


	def is_authenticated(self):
		return True


	def is_active(self):
		return True


	def is_anonymous(self):
		return False


	def get_id(self):
		return str(self.id)
