# Dependencies
# import pandas as pd
import tweepy
import time
import json
import random

#  MY Twitter API Keys
consumer_key = "PrTaNTbUUqLsUEthyElrcyG75" # MWE
consumer_secret = "QuPXbrTfaqBAVmUyGthxp4fXnALe24VuCjbmuFk8QzZwrsUUCM" # MWE
access_token = "171737379-p2BIU07JLdcjAuqMr19T8sY040VfvQFDybueyvjT" # MWE
access_token_secret =  "SiXYtwPYmu5r0kixMFJc59CSXt2Tv2zTy1zxr6NBVtUZL"

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]


# Create function for tweeting
def HappyItUp():

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
while(True):
    HappyItUp()
    time.sleep(60)
