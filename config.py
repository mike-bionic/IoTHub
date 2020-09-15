class Config:
	FLASK_ENV = 'development'
	TESTING = True
	SECRET_KEY = "&*ygioH(&G7oub))onf43nf03p4fn0u3b5npf"

	# Database
	SQLALCHEMY_DATABASE_URI = "sqlite:///IoTHub.db"
	UPLOAD_FOLDER = "static/post_uploads"