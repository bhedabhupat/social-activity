import tweepy
from tweepy import OAuthHandler

consumer_key = 'BvR9GWViH6r35PXtNHkV5MCxd '
consumer_secret = '2R6vK7nCsWIYneFgmlvBQUSbajD1djiYMIFLwwElZMYaa3r6Q8'
access_token = '253186422-cLKin1QKmjbezSaBg6iAYYUd0jyGT05NLzf3hQTJ'
access_secret = 'U2emZn44k7D3cLYS1QEBOQafk5hIVgptqTyt1Jkmat0qa'

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.followers).items(10):
    # Process a single status
    print(status)