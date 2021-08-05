import requests
import json


#https://developer.webex.com/docs/api/getting-started
bearer_token = "put access token here"
room_id = "put room id here"


def post(msg):
    url = "https://webexapis.com/v1/messages"

    headers = {
        'Authorization': 'Bearer ' + bearer_token
    }

    data = {
        "text" : msg,
        "roomId" : room_id
    }

    response = requests.post(url, headers=headers, data=data)

    return response.json()


def get():
    url = "https://webexapis.com/v1/rooms"

    headers = {
        'Authorization': 'Bearer ' + bearer_token
    }
    response = requests.get(url, headers=headers)

    return response.json()


def main():
    rooms = get()
    print(json.dumps(rooms,indent=2))
    message = post("Hello World")
    print(json.dumps(message,indent=2))
    
if __name__ == '__main__':
    main()