import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
json = json.loads(response.text)

print(response.text)
print(json)
