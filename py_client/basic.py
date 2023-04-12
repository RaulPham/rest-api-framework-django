import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

getResponse = requests.get(endpoint, json = {"query": "Hello World"})
print(getResponse.json()["message"])
# print(getResponse.status_code)#
