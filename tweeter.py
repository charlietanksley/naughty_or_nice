# tweeter.py
import json
import tweet_analyzer
import twitter

class Tweeter(object):
    def __init__(self, username, count=200):
        self._username = username
        self._tweet_count = count
        self._tweets = None

    def naughty_count(self):
        return tweet_analyzer.naughty_count(self.tweets())

    def set_tweets(self):
        tweets = twitter.tweets_by(str(self._username), self._tweet_count)
        self._tweets = tweets

        return tweets

    def to_json(self):
        return json.dumps({'username': self._username,
                           'naughty_count': self.naughty_count()})

    def tweets(self):
        if self._tweets == None:
            self.set_tweets()
            return self._tweets
        else:
            return self._tweets
