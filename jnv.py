import subprocess
from subprocess import Popen
import json
import requests


def colors(f):
	cmd = "curl"+" " +"-d" +"'"+'{"client_id":"###############","client_secret":"###############################################","audience":"http://homeexercise.volumental.com/","grant_type":"client_credentials"}'+"'" + " -H"+' "content-type: application/json"'+" -X POST  https://volumental.eu.auth0.com/oauth/token"
	proc = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE)
	t = proc.communicate()
	jsob = json.loads(t[0])
	tok= 'Bearer '+jsob['access_token'] 
	url = 'https://homeexercise.volumental.com/colors/images'
	heads = { 'Authorization' : tok, }
	response = requests.post(url,headers=heads,data = f)
	result = response.text
	re = json.loads(result)
	li = []
	for i in re:
		c = '#%02x%02x%02x' % (i['R'],i['G'],i['B'])
		li.append(c)
	return li
	
		




