import requests

endpoint= "http://localhost:8000/api/?q=cedricprogrammeur"

reponse = requests.get(endpoint)
print(reponse.json())
print(reponse.status_code)