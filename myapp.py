import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"

# agar koi id ke sath request krta h to usi id ka data mile nhi to pura data mil jaye


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data()  # function ko call krna h

# Note:==> ek ek kreke function ko call krna h yha remember it


def post_data():
    data = {
        'name': 'Raman',
        'roll': 18,
        'city': 'Kabul'
    }
    headers = {'content-Type': 'application/json'} # yha content type batana padega hame kya data bhej rhe
    json_data = json.dumps(data)  # convert it into json_data
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


post_data()


def update_data():
    data = {
        'id': 2,
        'name': 'Kishan',
        'roll': 11,
        'city': 'Pratapgarh'
    }
    json_data = json.dumps(data)  # convert it into json_data
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()


def delete_data():
    data = {
        'id': 4
    }
    json_data = json.dumps(data)  # convert it into json_data
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print("deleted data: ", data)

# delete_data()
