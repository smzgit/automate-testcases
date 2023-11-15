import requests


def get_all_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    data = requests.get(url=url)
    if data.status_code == 200:
        return data.json()
    else:
        raise Exception('failed to get users')
