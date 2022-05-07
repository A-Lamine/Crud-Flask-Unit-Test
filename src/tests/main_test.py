import requests

Get = requests.get('http://127.0.0.1:5000/').status_code
if Get == 200:
    print(Get, "Le test est ok ✅")
else:
    print(Get, "Le test est ko ❌")

Post = requests.post('http://127.0.0.1:5000/insert',
                     json={'url': 'Adventure', 'title': 'Wonder Woman'}).status_code
if Post == 201:
    print(Post, "Le test est ok ✅")
else:
    print(Post, "Le test est ko ❌")

Put = requests.put('http://127.0.0.1:5000/update',
                   json={'id': 1, 'url': 'AdventureUpdate', 'title': 'Wonder Woman'}).status_code
if Put == 200:
    print(Put, "Le test est ok ✅")
else:
    print(Put, "Le test est ko ❌")

Delete = requests.delete('http://127.0.0.1:5000/delete/1/').status_code
if Delete == 200:
    print(Delete, "Le test est ok ✅")
else:
    print(Delete, "Le test est ko ❌")
