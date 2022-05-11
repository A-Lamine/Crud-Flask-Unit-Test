from pyexpat import model
import requests


Get = requests.get('http://127.0.0.1:5000/').status_code
if Get == 200:
    print(Get, "Le Get est ok ✅")
else:
    print(Get, "Le Get est ko ❌")

Post = requests.post('http://127.0.0.1:5000/insert',
                     json={'url': 'www.Youtube.com', 'title': 'Youtube'}).status_code
if Post == 201:
    print(Post, "Le Post est ok ✅")
else:
    print(Post, "Le Post est ko ❌")

Put = requests.put('http://127.0.0.1:5000/update',
                   json={'id': 1, 'url': 'YoutubeUpdate', 'title': 'Youtube'}).status_code
if Put == 200:
    print(Put, "Le Put est ok ✅")
else:
    print(Put, "Le Put est ko ❌")

Delete = requests.delete('http://127.0.0.1:5000/delete/1/').status_code
if Delete == 200:
    print(Delete, "Le Delete est ok ✅")
else:
    print(Delete, "Le Delete est ko ❌")

