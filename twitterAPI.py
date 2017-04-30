import tweepy
import json
import os
from apikeys import ckey, csecret, atoken, asecret



def getTweets(query="cheese", lang="en", count="130", result_type="recent", filename="tweets.txt", geocode="53.721247,3.904416,300mi"):
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)

    # Specify your search parameters here
    results = api.search(q=query, lang=lang, count=count, result_type=result_type, geocode=geocode)

    filename = filename
    tweets = []

    for result in results:
        tweets.append(result.text)

    return tweets

# getTweets()
