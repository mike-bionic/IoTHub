from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired

class DeviceForm(FlaskForm):
	device_name = StringField('Device name:',validators=[DataRequired()])
	device_key = StringField('Device name:',validators=[DataRequired()])
	description = StringField('Description:')