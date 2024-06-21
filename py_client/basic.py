import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title": "title", "content": "hello wold!", "price": "22"})
print(get_response.json())
