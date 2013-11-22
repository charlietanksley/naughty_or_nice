from flask import Flask, send_from_directory
import tweet_analyzer
from tweeter import Tweeter
from twitter import tweets_by

app = Flask(__name__)

@app.route('/api/naughty_count/<username>')
def naughty_count(username):
    return Tweeter(username).to_json()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()
