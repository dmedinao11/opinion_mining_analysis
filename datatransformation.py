# -*- coding: utf-8 -*-
"""dataTransformation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10dG1qRS0QbpmZLiUSvWjaWYymA6xkl43

# **Limpieza de datos**
"""

import pandas as pd
from textblob import TextBlob
from datetime import datetime
df = pd.read_csv('data.csv')

"""**Eliminando columnas sin importancia**"""

df.drop(['conversation_id', 'created_at', "time",	"timezone", "user_id",	"username",	"name",	"place", "mentions",	"urls"	,"photos",	"replies_count",	"retweets_count",	"likes_count"	,"hashtags"	,"cashtags", "retweet", "quote_url",	"video",	"thumbnail","source" ,"near"	,"user_rt_id","user_rt","retweet_id"	,"reply_to"	,"retweet_date"	,"translate"	,"trans_src"	,"trans_dest"  ], axis=1, inplace=True)

"""**Eliminando datos repetidos**"""

df.drop_duplicates(subset ="id", keep = False, inplace = True)
df = df.set_index("id")

"""**Eliminando lenguajes diferentes al Español e inglés**"""

df = df[(df['language'] == "es") | (df['language'] == "en")]

df.to_csv('clean_data_final.csv')

"""**Merge**

"""

df1 = pd.read_csv('trans_tweet.csv')
df2 = pd.read_csv('trans_tweet2.csv')
df3 = pd.read_csv('trans_tweet3.csv')

frames = [df1, df2, df3]
df4 = pd.concat(frames)
df4.drop_duplicates(subset ="id", keep = False, inplace = True)
df4 = df4.set_index("id")
df4.to_csv("mergeTrans.csv")

"""**Limpiar tweets**

"""

import re

def cleanHash(hashtag: str):
    hashtag = re.sub("[-_#]"," ", hashtag)
    pattern2 = "(?=[A-Z])"
    hashtag = re.split(pattern2, hashtag)
    print(hashtag)
    return " ".join(hashtag).strip()

def cleanTweet(tweet):
    hashtags = re.findall(r"#[a-zA-Z0-9_\-]+\b", tweet)
    
    if len(hashtags) > 0:
        cleanHashtags = map(cleanHash, hashtags)
        cleanHashtags = list(cleanHashtags)
        for i in range(len(hashtags)):
            tweet = tweet.replace(hashtags[i], cleanHashtags[i])
            
    tweet = tweet.replace("@", "")

    return tweet

a = ["Indignante lo que pasa en nuestro país #covid19, asesinan a niños, jóvenes, líderes. Las balas están matando más que el covid, pero indigna aún más ver qué a nadie parece importarle #JusticiaParaLlanoVerde #QuienLosMato", "#ManizalesEnVivo Pará tu bienestar y cuidado Confa lleva el médico hasta tu casa #TeCuidoMeCuidas #QuedateEnCasa #contigocontodo en Manizales, Caldas  https://t.co/o71a8uSqhV"]

for tweet in a:
    print(cleanTweet(tweet))

"""**Traducción inglés**"""

df = df[df["trans_tweet"].isnull()]

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

df["trans_tweet"] = df.apply(translateTweet, axis=1)
df.to_csv("trans_tweet3.csv")

"""**PNL**"""

def classifierPolarity(polarity):
  if polarity >= -1 and polarity < -0.6:
      return "Muy negativa"
  elif polarity >= -0.6 and polarity < -0.2:
      return "Negativa"
  elif polarity >= -0.2 and polarity <= 0.2:
      return "Neutra"
  elif polarity > 0.2 and polarity <= 0.6:
      return "Positiva"
  else:
      return "Muy positiva"
      
def classifierSubjectivity(subjectivity):
  if subjectivity >= 0 and subjectivity < 0.2:
      return "Muy objetivo"
  elif subjectivity >= 0.2 and subjectivity < 0.4:
      return "Objetivo"
  elif subjectivity >= 0.4 and subjectivity <= 0.6:
      return "Neutra"
  elif subjectivity > 0.6 and subjectivity <= 0.8:
      return "Subjetivo"
  else:
      return "Muy subjetivo"




def getSentiment(row):
  tb = TextBlob(row["trans_tweet"])
  row["polarity"] = tb.sentiment.polarity
  row["subjectivity"] = tb.sentiment.subjectivity
  row["polarity_class"] = classifierPolarity(tb.sentiment.polarity)
  row["subjectivity_class"] = classifierSubjectivity(tb.sentiment.subjectivity)
  return row


df = df.apply(getSentiment,axis=1)

df.to_csv('data_pnl.csv')

df.head()

"""**Sand box**"""

df = df.drop(df.columns[0], axis=1)
df.head()
df = pd.read_csv('mergeTrans.csv')
trans = df[df["trans_tweet"].notnull()]
trans.drop_duplicates(subset ="id", keep = False, inplace = True)
trans["id"].value_counts()
df = trans.set_index("id")
df.to_csv('trans_tweet_final.csv')
df[df["polarity_class"] == "Muy negativa"].head()
len(df[df["polarity_class"] == "Muy positiva"].index)

import pandas as pd

df = pd.read_csv("data_pnl.csv")
df = df.drop(df.columns[0], axis=1)
df = df.set_index("id")

df = df.head()
df.to_excel("Tabla.xlsx")