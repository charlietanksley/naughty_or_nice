# tweet_analyzer.py
import re
import dictionary

def tweet_bodies(tweets):
    return [tweet[u'text'] for tweet in tweets]

def stringify_array(array):
    return ' '.join(array)

def naughty_tweets(tweets):
    '''
    Takes an array of tweets (Twitter objects) and counts the number of "naughty" words in them.
    '''
    regex = re.compile(dictionary.naughty_word_pattern)
    matching_tweets = [tweet for tweet in tweets if regex.search(tweet[u'text'])]
    return matching_tweets
