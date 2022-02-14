import requests
get_response = requests.get("http://192.168.68.82:5000/model/labels")
print(get_response)
#print(response.json())

#upload an image for classification
url = 'http://192.168.68.82:5000/model/predict?threshold=0.7'
headerObj = {'accept':'application/json'}
fileObj = {'image': open('IMG_2178.jpeg', 'rb')}
post_response = requests.post(url, headers = headerObj, files = fileObj)
print(post_response.json())


