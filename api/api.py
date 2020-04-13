from flask import Flask, request
import random
from Predict import *
import smtplib, ssl, email

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


app = Flask(__name__)
port = 465
password = 'WTPROJECT2020'
email = 'wtproject2020'
subject = "Pictionary! Drawing"
body = "Hope you had fun!"


@app.route('/api/canvas_img', methods=['POST'])
def store_canvas():
	img = request.get_data()
	f = open('your_drawing.jpeg','wb')
	f.write(img)
	f.close()
	pred = Predict('your_drawing.jpeg') 
	if (pred[1] > 0.5):
		return pred[0]
	return

@app.route('/api/object_name')
def get_object_name():
	x = random.randint(0,9)
	objects = ['apple','bowtie','candle','door','envelope','fish', 'guitar','ice cream','lightning','moon','mountain','star','tent','toothbrush','wristwatch']
	return objects[x]


@app.route('/api/mail_drawing',methods=['POST'])
def mail_drawing():
	emailTo = request.data.decode('utf-8')
	
	message = MIMEMultipart()
	message["From"] = email
	message["To"] = emailTo
	message["Subject"] = subject	

	message.attach(MIMEText(body, "plain"))
	attachment = 'your_drawing.jpeg'
	
	img_data = open(attachment, "rb").read()
	image = MIMEImage(img_data,name=attachment)
	message.attach(image)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login(email, password)
		server.sendmail(email,emailTo,message.as_string())

	return 'Success'