from asyncio.log import logger
import requests
import json

URL='http://127.0.0.1:8000/serialized/'
def post_data():
    data={
        'username':'harshita',
        'email':'abc@gmail.co',
        'pwd':'234',
        'cpwd':'234'
    }
    headers = {'Content-Type': 'application/json'}
    json_data=json.dumps(data)
   
    response = requests.post(url=URL,data=json_data)
    data=response.json()
    print(data)


post_data()