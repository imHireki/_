"""
core utils
"""
import json


def get_secret(name):
    """ Get my local project's secrets """

    with open('secret.json') as json_file:
        data = json.load(json_file)
        secret = data.get(name)
        return secret

