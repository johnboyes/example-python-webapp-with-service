
import requests

from flask import Flask

app = Flask(__name__)

@app.route('/')
def user_name():

    # import os

    # proxy = 'https://jsonplaceholder-typicode-com-wtsdqse.hoverfly.io'

    # os.environ['http_proxy'] = proxy
    # os.environ['HTTP_PROXY'] = proxy
    # os.environ['https_proxy'] = proxy
    # os.environ['HTTPS_PROXY'] = proxy

    # os.environ.pop("http_proxy")
    # os.environ.pop("HTTP_PROXY")
    # os.environ.pop("https_proxy")
    # os.environ.pop("HTTPS_PROXY")


    # proxies = {
    #     'http': 'http://jsonplaceholder-typicode-com-wtsdqse.hoverfly.io',
    #     'https': 'http://jsonplaceholder-typicode-com-wtsdqse.hoverfly.io',
    # }

    # users = requests.get('http://jsonplaceholder.typicode.com/users', proxies=proxies, verify=False)
    users = requests.get('http://jsonplaceholder.typicode.com/users')
    # return users
    # users = requests.get('https://jsonplaceholder-typicode-com-wtsdqse.hoverfly.io/users', verify=False)
    return users.json()[0]['name']
