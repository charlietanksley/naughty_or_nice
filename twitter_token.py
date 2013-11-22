# twitter_token.py
from os import getenv, path
from base64 import b64encode
import requests

# https://dev.twitter.com/docs/auth/application-only-auth
def twitter_key():
    if path.isfile('secrets.py'):
        import secrets
        return secrets.TWITTER_CONSUMER_KEY
    else:
        return getenv('TWITTER_CONSUMER_KEY')

def twitter_secret():
    if path.isfile('secrets.py'):
        import secrets
        return secrets.TWITTER_CONSUMER_SECRET
    else:
        return getenv('TWITTER_CONSUMER_SECRET')

def twitter_credentials():
    key = twitter_key()
    secret = twitter_secret()
    return b64encode(':'.join([key, secret]))

def obtain_twitter_bearer_token():
    url = 'https://api.twitter.com/oauth2/token'
    headers = {'Authorization': ' '.join(['Basic', twitter_credentials()]),
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    body = 'grant_type=client_credentials'

    response = requests.post(url, data=body, headers=headers)
    return str(response.json()[u'access_token'])
