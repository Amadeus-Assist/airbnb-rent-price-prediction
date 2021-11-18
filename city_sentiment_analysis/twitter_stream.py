from datetime import datetime
import tweepy
from prettytable import PrettyTable
from textblob import TextBlob

# Twitter Credentials
ACCESS_TOKEN = "1133350537204834305-Wft7EpVTfwLgYSfJQdH2gzxiEfsP9o"
ACCESS_TOKEN_SECRET = "gme5J65D28mA4wdISfPaaKQqmhFZUqJAwXtguiJRbcgn4"
CONSUMER_KEY = "Ej6ZAEym4PWa5BRtxSepTOaM0"
CONSUMER_SECRET = "tbBwCbrG4xq5z4In3B6N76WJh6Iox1fMwAnk2sxJb3Silnxp2M"


AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
API = tweepy.API(AUTH)


def get_tweets(geocode, aggr='sum'):
    i = 1
    score_sum = 0
    pretty_table = PrettyTable()
    pretty_table.field_names = ["Count", "ID", "Date", "Text", "Score"]

    for tweet in tweepy.Cursor(API.search, q="*", count=200, geocode=geocode, lang="en").items(1000):
        tweet_id = tweet.id
        date = datetime.strptime(str(tweet.created_at)[
                                 :10], '%Y-%m-%d').strftime('%d-%m-%Y')
        text = tweet.text
        score = round(TextBlob(text).sentiment.polarity, 4)
        pretty_table.add_row([i, tweet_id, date, text, score])
        i = i + 1
        score_sum = score_sum + score
    print(pretty_table)
    if aggr == 'sum':
        return score_sum
    elif aggr == 'average':
        return score_sum / i
