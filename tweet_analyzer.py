# tweet_analyzer.py
import re
import dictionary

def tweet_bodies(tweets):
    return [tweet[u'text'] for tweet in tweets]

def stringify_array(array):
    return ' '.join(array)

def naughty_count(tweets):
    '''
    Takes an array of tweets (Twitter objects) and counts the number of "naughty" words in them.
    '''
    regex = re.compile(dictionary.naughty_word_pattern)
    bodies = tweet_bodies(tweets)
    canon = stringify_array(bodies)
    return len(regex.findall(canon))
