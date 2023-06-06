from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'Karthik'
app.config['MAIL_PASSWORD'] = 'sdmit@123'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = '19b03@sdmit.in'

mail = Mail(app)
