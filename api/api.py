from flask import Flask, request
import random
from Predict import *

app = Flask(__name__)

@app.route('/api/canvas_img', methods=['POST'])
def store_canvas():
	img = request.get_data()
	f = open('sample.jpeg','wb')
	f.write(img)
	f.close()
	pred = Predict('sample.jpeg') 
	if (pred[1] > 0.5):
		return pred[0]
	return

@app.route('/api/object_name')
def get_object_name():
	x = random.randint(0,9)
	objects = ['apple','bowtie','candle','door','envelope','fish', 'guitar','ice cream','lightning','moon','mountain','star','tent','toothbrush','wristwatch']
	return objects[x]