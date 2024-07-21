import tweepy
import random

def random_line(afile):
    # Get a random line from given file
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

def tweet(client):
    # Post tweet
    lyrics_file = open("lyrics.txt", "r")
    randomLyric = random_line(lyrics_file)
    try:
        response = client.create_tweet(
            text = randomLyric
        )
    except:
        tweet(client)
    # print(f"https://twitter.com/user/status/{response.data['id']}")

def main():
    # Authenticate to Twitter
    bearer_token = "REDACTED_BEARER_TOKEN"
    consumer_key="REDACTED_CONSUMER_KEY"
    consumer_secret="REDACTED_CONSUMER_SECRET"
    access_token="REDACTD_ACCESS_TOKEN"
    access_token_secret="REDACTED_ACCESS_TOKEN_SECRET"

    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

    tweet(client)
