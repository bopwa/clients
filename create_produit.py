import requests
endpoint= "http://localhost:8000/api/"

data = {
    'name': "avocat",
    'price':1000,
    'description': "fruit"
}
reponse = requests.get(endpoint)
print(reponse.json())
print(reponse.status_code)