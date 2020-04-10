from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/api/canvas_img', methods=['POST'])
def store_canvas():
	img = request.get_data()
	f = open('sample.jpeg','wb')
	f.write(img)
	f.close()
	#preprocess image
	#pass through CNN
	#get index of max probability
	#find matching entry in list of objects 
	x = random.randint(0,9)
	objects = ['apple','cat','dog','shark','sea','tree','flower','sun','moon','scythe']
	return objects[x]


@app.route('/api/object_name')
def get_object_name():
	x = random.randint(0,9)
	objects = ['apple','cat','dog','shark','sea','tree','flower','sun','moon','scythe']
	return objects[x]