from datetime import date,datetime,time
from flask_login import UserMixin
from main import db
from main import login_manager


@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(50),unique=True)
	full_name = db.Column(db.String(100))
	password = db.Column(db.String(100),nullable=False)
	email = db.Column(db.String(225))
	phone_number = db.Column(db.String(25))
	address = db.Column(db.String(100))
	city_id = db.Column(db.Integer,db.ForeignKey("city.id"))
	devices = db.relationship('Devices',backref='user',lazy=True)
	def __repr__ (self):
		return f"User('{self.username}')"


class City(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	country_name = db.Column(db.String(100),nullable=False)
	city_name = db.Column(db.String(500))
	user = db.relationship('User',backref='city',lazy=True)


class Devices(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	device_name = db.Column(db.String(100),nullable=False)
	device_key = db.Column(db.String(255),nullable=False)
	description = db.Column(db.String(500))
	date = db.Column(db.DateTime,default=datetime.now)
	user_id = db.Column(db.Integer,db.ForeignKey("user.id"))	
	values = db.relationship('Values',backref='device',lazy=True)


class Values(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	value = db.Column(db.String(255),nullable=False)
	date = db.Column(db.DateTime,default=datetime.now)
	device_id = db.Column(db.Integer,db.ForeignKey("devices.id")) 