import urllib.request
opener = urllib.request.build_opener()
response =  opener.open ("https://vk.com/")
print (response.read())
print("=======================================")
import requests
response = requests.get('https://vk.com/')
print (type(response.content))

