import tweepy
import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

def tweet(client):
    testTweet="Test tweet from KGW Lyric Bot"
    lyrics_file = open("lyrics.txt", "r")
    randomLyric=random_line(lyrics_file)
    print(randomLyric)
    try:
        response = client.create_tweet(
            text=randomLyric
        )
    except:
        tweet(client)
    print(f"https://twitter.com/user/status/{response.data['id']}")

def main():
    # Authenticate to Twitter
    bearer_token = "AAAAAAAAAAAAAAAAAAAAALnGuwEAAAAAQfbCoSXtr1puL9Ik3LRYCuCskts%3D1J82bVlsTezAp94nblQjxHSq5BTzjYaLHl7EkrEFV41qwiYaN4"
    consumer_key="U15tN9gSWs8D6si8onoYYA6ff"
    consumer_secret="weaA4PkY5SS3fo9d2rhy6NcOcsHo3gIlND6tDAcn46hhdHJgaZ"
    access_token="1814718100270686209-FiA1jfLCfrAv1pEBccI0nwuPg2PTwm"
    access_token_secret="um1Na68LpKJuiWq5ryLnGK2h0XIQ7KB1yp4haq0Bmx292"

    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

    tweet(client)
