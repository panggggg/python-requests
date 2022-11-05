import requests

def request_method(data):
    return requests.request(method=data["method"], url=data["endpoint"], headers=data["header"], data=data["payload"]).json()