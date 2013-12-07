# tweeter.py
import json
import tweet_analyzer
import twitter

class Tweeter(object):
    def __init__(self, username, count=200):
        self._username = username
        self._tweet_count = count
        self._tweets = None
        self._naughty_tweets = None

    def naughty_tweets(self):
        if self._naughty_tweets == None:
            self._naughty_tweets = tweet_analyzer.naughty_tweets(self.tweets())
            return self._naughty_tweets
        else:
            return self._naughty_tweets

    def naughty_count(self):
        return len(self.naughty_tweets())

    def set_tweets(self):
        tweets = twitter.tweets_by(str(self._username), self._tweet_count)
        self._tweets = tweets

        return tweets

    def to_json(self):
        return json.dumps({'username': self._username,
                           'naughtyCount': self.naughty_count(),
                           'naughtyTweets': self.naughty_tweets(),
                           'tweetsConsidered': len(self.tweets())})

    def tweets(self):
        if self._tweets == None:
            self.set_tweets()
            return self._tweets
        else:
            return self._tweets
