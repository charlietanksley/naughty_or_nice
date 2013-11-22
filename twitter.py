# twitter.py
from os import getenv, path
from base64 import b64encode

# https://dev.twitter.com/docs/auth/application-only-auth
def twitter_credentials():
    key = twitter_key()
    secret = twitter_secret()
    return b64encode(':'.join([key, secret]))

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
