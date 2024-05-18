import requests

res = requests.put("http://127.0.0.1:3000/api/courses/2", {"name": "Golang", "videos": 5})
print(res.json())
