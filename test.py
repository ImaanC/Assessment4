import requests

import requests
BASE = "http://127.0.0.1:5000/"

data = [{"name":"Sam","surname":"James","age":23,"gender": "female"},
        {"name":"Carl","surname":"Gallagher","age":22,"gender": "male"},
        {"name":"Timothee","surname":"Chalamet","age":25,"gender": "male"}]

for i in range(len(data)):
    response = requests.put(BASE + "student/" +str(i), data[i])
    print(response.json())

response = requests.patch(BASE + "student/1", {"name":"Carl","surname":"Gallagher","age":23,"gender": "male"})
print(response.json())

input()

response = requests.get(BASE + "student/2")
print(response.json())

input()

response = requests.delete(BASE + "student/0")
print(response.json())