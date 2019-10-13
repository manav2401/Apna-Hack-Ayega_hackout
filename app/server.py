from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
import json
import boto3
import botocore

app = Flask(__name__)

ACCESS_KEY=''
SECRET_KEY=''
BUCKET_NAME='hackoutpothole'

@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		data = request.form
		username=data['username']
		#if welcomeLogin(data['username']):
		str=username+'/'+'read'
		return redirect(url_for('read', user=username))
		#else:
		#print("Error")
		#return render_template('error.html')
	
@app.route("/features", methods=['GET'])
def features():

	s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
	#s3.upload_file("co.txt", "hackoutpothole", "co.txt")
	#bucket = s3.Bucket(BUCKET_NAME)
	s3.Bucket(BUCKET_NAME).download_file('co.txt', 'co.txt')
	fileName = "co.txt"
	with open(fileName, "r") as file:
		data = file.read()
		result = data.split("\n")
		count=0
		cnt = 0
		vari = []
		len_result = len(result)
		for s in result:
			count = count + 1
			if count == len_result:
				break
			if s[len(s)-1] == "1":
				c1 = s.split(" ", 1)
				c2 = c1[0].split(",", 1)
				#print(c2)
				vari.append(["Pothole", float(c2[0]), float(c2[1]) ,cnt])
				final = "[Potholes," + c2[0] + "," + c2[1] + "," + str(cnt) + "],"
				opFile = open("output.txt", "a")
				opFile.write(final)
				cnt = cnt + 1

	#info = "Pothole"
	#lat = 23.187247
	#lon = 72.627666
	#vari = [info, lat, lon, 0]
	#print(vari)
	return render_template('features.html', vari=vari)


@app.route("/advanced", methods=['GET'])
def advanced():
	if request.method == 'GET':
		return render_template('advanced.html')

@app.route("/statistics", methods=['GET'])
def statistics():
	if request.method == 'GET':
		return render_template('statistics.html')

@app.route("/map")
def map():

	fileName = "co.txt"
	with open(fileName, "r") as file:
		data = file.read()
		result = data.split("\n")
		count=0
		cnt = 0
		vari = []
		len_result = len(result)
		for s in result:
			count = count + 1
			if count == len_result:
				break
			if s[len(s)-1] == "1":
				c1 = s.split(" ", 1)
				c2 = c1[0].split(",", 1)
				#print(c2)
				vari.append(["Pothole", float(c2[0]), float(c2[1]) ,cnt])
				final = "[Potholes," + c2[0] + "," + c2[1] + "," + str(cnt) + "],"
				opFile = open("output.txt", "a")
				opFile.write(final)
				cnt = cnt + 1

	#info = "Pothole"
	#lat = 23.187247
	#lon = 72.627666
	#vari = [info, lat, lon, 0]
	print(vari)
	return render_template('maps.html', vari=vari)

@app.route("/dot.png")
def image():
	filename = 'dot1.png'
	return send_file(filename, mimetype='image/png')

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('welcome.html')
	elif request.method == 'POST':
		data = request.form
		username = data['username']
		welcomeRegister(data['username'])
		return redirect(url_for('read', user=username))
		

#@app.route("/<user>/read", methods=['GET', 'POST'])
#def read(user):
#	if request.method == 'GET':
#		return render_template('read.html')
#	elif request.method == 'POST':
#		book_data, book_category = readNew(user, request.form['book_name'])
#		return render_template('readAns.html', user=user, book_data=book_data, book_category=book_category)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3800, debug=True, threaded=True)