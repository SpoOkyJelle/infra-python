import requests



print('Welcome to the Swapi! Enter the name of the character:')

def callback(name):
    response = requests.get("https://swapi.dev/api/people/" + name + '/')
    if response.status_code != 404:
        print(response.json()['name'])
    
    else:
        print('Error!')
    


callback(input())

