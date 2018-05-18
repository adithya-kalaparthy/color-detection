import mimetypes
import os.path
import requests
def download(authto,fid):
	accessToken = authto
	fileId = fid
	fileInf = requests.get(
	    "https://www.googleapis.com/drive/v3/files/" + fileId,
	    headers={"Authorization": "Bearer " + accessToken},
	)
	filename = fileInf.json()["name"]
	temp, ext = os.path.splitext(filename)
	filename = filename if ext != "" else filename + mimetypes.guess_extension(fileInf.json()["mimeType"])
	r = requests.get(
	    "https://www.googleapis.com/drive/v3/files/" + fileId + "?alt=media",
	    headers={"Authorization": "Bearer " + accessToken},
	)
	f = r.content
	return f
