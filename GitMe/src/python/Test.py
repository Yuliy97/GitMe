import json
import requests
from toDB import write_to_user, remove_from_user

root = "http://localhost:5000"
username = "jgormley6"
password = "JG9671166soccerfan"
data = {}
data["username"] = username
data["password"] = password

def test():
    url = root + "/users/jgormley6"
    r = requests.get(url)
    user = json.loads(r.content)
    print(json.dumps(user, indent=4))

    url = root + "/users/" + username + "/repository"
    r = requests.get(url)
    repos = json.loads(r.content)
    print(json.dumps(repos, indent=4))

def old2test():
    url = root + "/update"
    r = requests.post(url, params=data)
    
    url = root + "/users/" + username
    r = requests.get(url, params=data)
    users = json.loads(r.content)
    print(json.dumps(users, indent=4))

    url = url + "/repository"
    r = requests.get(url)
    repos = json.loads(r.content)
    print(json.dumps(repos, indent=4))

def oldtest():


    #write_to_user(username="jgormley6", password="JG9671166soccerfan")
    
    # remove_from_user("jgormley6")
    url = "http://localhost:5000/users/jgormley6"
    params={'username': username, 'password': password}
    r = requests.post(url, params=params)
    r = requests.get(url)
    users = json.loads(r.content)
    print(json.dumps(users, indent=4))


    url = "http://localhost:5000/users/jgormley6/repository"
    r = requests.post(url, params=params)


    r = requests.get(url)
    user = json.loads(r.content)
    print(json.dumps(user, indent=4))

test()
