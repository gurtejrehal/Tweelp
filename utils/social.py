import tweepy
from twilio.rest import Client
import os

consumer_key = os.environ.get("SOCIAL_AUTH_TWITTER_KEY", None)
consumer_secret = os.environ.get("SOCIAL_AUTH_TWITTER_SECRET", None)
access_key = os.environ.get("ACCESS_KEY", None)
access_secret = os.environ.get("ACCESS_SECRET", None)

account_sid = os.environ.get("ACCOUNT_SID", None)
auth_token = os.environ.get("AUTH_TOKEN", None)


def social_media_scrape(keyword):
    result = []
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    tweets = api.search(keyword, count=20)
    for tweet in tweets:
        temp = {}
        temp['timestamp'] = tweet.user.created_at.isoformat()
        temp['username'] = tweet.user.name
        temp['screen_name'] = tweet.user.screen_name
        temp['tweet_url'] = f"https://twitter.com/twitter/statuses/{tweet.id}"
        temp['text'] = tweet.text
        temp['likes'] = tweet.favorite_count
        temp['retweets'] = tweet.retweet_count

        l_hashtags = []
        for i in tweet.entities['hashtags']:
            l_hashtags.append(i['text'])

        temp['hashtags'] = ",".join(l_hashtags)
        result.append(temp)
    return result


def send_message(tweet):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=tweet, from_='+14344338069', to='+919064226537')
    return message.sid


def send_alerts():
    x = send_message("Stay alert!")
    print(x)

