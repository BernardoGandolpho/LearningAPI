import requests
import json

# URLs
api_url = "https://jsonplaceholder.typicode.com/todos"
api_url_id = "https://jsonplaceholder.typicode.com/todos/1"


# GET
response = requests.get(api_url_id)

print(response.status_code)
print(response.json())


# POST
todo = {"userId": 1, "title": "Buy milk", "completed": False}

response = requests.post(api_url, json=todo)

print(response.status_code)
print(response.json())


# POST with headers
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}

response = requests.post(api_url, data=json.dumps(todo), headers=headers)

print(response.status_code)
print(response.json())
