from flask import Flask, request

app = Flask(__name__)

@app.route('/canvas_img', methods=['POST'])
def store_canvas():
	img = request.get_data()
	f = open('sample.jpeg','wb')
	f.write(img)
	f.close()
	return 'Success!'