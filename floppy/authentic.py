import requests
import json

payload = {
    'username':'basicUser',
    'password':'basicUser'
}
payload = json.dumps(payload)

r = requests.post('http://localhost:8080/login', data = payload)
print(r.headers['token'])
