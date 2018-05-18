import os
import flask
from flask import Flask, render_template, request
from hg import download
from jnv import colors
from base64 import b64encode
app = Flask(__name__)
global images
images = []
global j
j=[]
global count 
count = 0
global countp
countp =0
def colo():
	with open("colors.jpg") as imgf:
		im = imgf.read()
		imst = b64encode(im)
	return imst
@app.route("/")
def index():
	return render_template("upload.html")

@app.route('/upload',methods=['POST'])
def upload():
	global images
	images = []
	global j
	j=[]
	ims = request.files.getlist("file")
	for i in range(len(ims)):
		imr = ims[i].read()
		images.append(imr)
		col = colors(imr)
		j.append(col)	
	bim2 = colo()
	return render_template("complete.html",arr=["white","white","white","white","white"],image=bim2)
	
@app.route('/gdrive',methods=['POST'])
def gdrive():
	global images
	images = []
	global j
	j=[]
	arr = request.form.getlist('auidarray')
	arr = str(arr.pop(0))
	li=arr.split(',')
	token = li.pop(0)
	images = [] 
	for i in li:
		files = download(token,i)
		images.append(files)
		col = colors(files)
		j.append(col)
	bim = colo()
	return render_template("complete.html",arr=["white","white","white","white","white"],image=bim)


@app.route('/complete/next')
def next():
	global count
	global images
	global j
	global countp
	if count>=len(images):
		count = 0
	else:
		pass
	jc = j[count]
	image = b64encode(images[count])
	countp = count
	count = count+1
	return render_template("complete.html",arr=jc,image=image)
@app.route('/complete/previous')
def previous():
	global count
	global images
	global j
	global countp
	if (abs(countp-1)>len(images)):
		countp = len(images)-1
	else: 
		countp = countp-1
	jc = j[countp]
	image = b64encode(images[countp])
	count = countp+1
	return render_template("complete.html",arr=jc,image=image)

if __name__ == "__main__":
	app.run(host="localhost", port=5000, debug = True)
