import pandas as pd
from textblob import TextBlob
from datetime import datetime


def translateTweet(row):
    if row["language"] == "en":
      return row["tweet"]
    
    tb = TextBlob(row["tweet"])

    try:
        tb = tb.translate(from_lang="es", to="en")
        print("[!] Translated", str(datetime.now()))
    except:
        print("[X] ERROR", str(datetime.now()))
        return None
    
    return str(tb)



df = pd.read_csv("untranslated.csv")
df = df.set_index("id")
df.drop(df.columns[0], axis=1, inplace=True)
df["trans_tweet"] = df.apply(translateTweet, axis=1)

df.to_csv("trans_tweet2.csv")