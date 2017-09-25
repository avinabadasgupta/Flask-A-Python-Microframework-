from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
@app.route('/')
def index():
   return render_template("client.html")
@app.route('/process',methods=['POST'])
def process():
	data=request.get_json()
	name=data['name'];
	age=data['age'];
	errorMessage="Invalid Name or Age"
	if name and age:
		if age.isnumeric():
			age=int(age);
			if age==0:
				return jsonify({'error':errorMessage})
			if age>=65:
				return jsonify({'name':name,'message':' You are a Senior'})
			else:
				return jsonify({'name':name,'message':' You are a Junior'})
		else:
			return jsonify({'error':errorMessage})
	return jsonify({'error':errorMessage})
if __name__ == '__main__':
   app.run(debug=True)