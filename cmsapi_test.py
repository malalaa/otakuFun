import requests

headers = {
   "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MTgzODA0NywianRpIjoiYWViYjVjNjEtNGJhZS00NDFlLTg2NjMtOWVhZjg2NDkxNzU0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlNDbzJQdlBhakVCTFpnajRFeUNLRTciLCJuYmYiOjE2OTE4MzgwNDcsImV4cCI6MTY5MTgzODk0N30.tkkWdGVXzgLFex1BTL50zSA4ClSiEHC_A3zdKiErE-s"
}
resp = requests.get("http://127.0.0.1:5000/cmsapi", headers=headers)
print(resp.text)