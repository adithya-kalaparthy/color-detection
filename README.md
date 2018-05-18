# color-detection

Hello There,


Thank You For Using This Application. This Is A Fun Application Which Uses An Api To Calculate The Most Prominent Colors Of Your Image Which Has Been Uploaded.

Prerequisites:

1. Python
2. flask
3. web-browser
4. curl

Note: The names of the files are not to be changed, if they are changed then please look in to the code and change the names of the files there as well.

Ways to use this api:

1. Firstly, start the api.py (python script) using "python api.py" in the terminal. This should start the flask api on your localhost:5000
2. Go to the web-browser and go to http://localhost:5000/
3. After 1&2 steps you should now be able to see upload.html page.
4. If you want to upload a picture which is in your computer please use "Browse" button which is in the 1st white band. After selecting required images please press "detect colors" in the same white band
5. If you want to upload a picture in your google drive please use "upload from google" button which is in the bottom white band. After selecting required images press "detect colors"
6. Now you must be redirected to "complete.html" page
7. This is the results page Please select "previous" or "upnext" as per your choice.
8. Whatever you select the image and the result corresponding to the image is displayed.
9. If you have selected only 3 photos and if you press "upnext" 4 times then the 1st picture of your selection is displayed. The same goes with previous as well.


Note: 	This application has been developed with Python 2.7.12 and tested in ubuntu 16.04, mozilla firefox.
	Due to confidentiality reasons the api key and Id for google have been removed. Please follow the link https://console.developers.google.com/api to generate api keys and credentials
	(Developer key, api-id, clientId are required) After generating the credentials please change the credentials in upload.html file
	The client secret and client id for volumental api have also been removed. Please generate seperate client credentials from volumental

