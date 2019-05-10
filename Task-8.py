# impporting modules requered for the programe
from flask import Flask, jsonify, request,abort
app = Flask(__name__)

# creating route and defining methods can used for this endpoint
@app.route('/', methods=['GET','POST'])
def hello_world():
	method = request.method
	if method == 'POST':
		name = request.json.get('name')
		return ("Hello, {}".format(name))
	else:
		abort(405)

#listening with port and host with debuging
app.run(host = '127.0.0.1', port='8080', debug=True)
