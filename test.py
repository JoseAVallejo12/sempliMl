#!env/bin/python3
import requests


# Response a newUser random using the request.get and parsing to object with json() method
params = requests.get('https://lv2394qpu0.execute-api.us-east-1.amazonaws.com/dev/user/random').json()
# Define the headers for sent an request to API clostering customer
headers = {'Content-Type': 'application/json'}
# Response a clostering user using the request.get and parsing to object with json() method
res = requests.post("https://lv2394qpu0.execute-api.us-east-1.amazonaws.com/dev/user/cluster", params=params, headers=headers).json()
# Print inf of user
print(f'user data sent: {params}')
# Print cluster user
print(f"clustering user: {res}")