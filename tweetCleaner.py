import pandas as pd
import re

def cleanHash(hashtag: str):
    hashtag = re.sub("[-_#]", " ", hashtag)
    return " ".join(re.split("(?=[A-Z])", hashtag)).strip()


def cleanTweet(tweet):
    hashtags = re.findall(r"#[a-zA-Z0-9_\-]+\b", tweet)

    if len(hashtags) > 0:
        cleanHashtags = map(cleanHash, hashtags)
        cleanHashtags = list(cleanHashtags)
        for i in range(len(hashtags)):
            tweet = tweet.replace(hashtags[i], cleanHashtags[i])

    tweet = tweet.replace("@", "")

    return tweet


df = pd.read_csv('clean_data_final.csv')
df["tweet"] = df["tweet"].apply(cleanTweet)
df.to_csv("tweet_cleaned.csv")