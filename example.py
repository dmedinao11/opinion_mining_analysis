""" # Configure
import twint


c = twint.Config()
#c.Search = "(# OR #nomascuarentena OR #wuhan OR #todovaaestarbien OR #BogotaACieloAbierto OR #COVID_19 OR #SARS_CoV_2 OR #vacuna OR #coronavirus OR #YoMeCuidoYoTeCuido OR #infectados OR #cuarentena OR #quedateencasa OR #JuntosEnLaPrevencion OR #autocuidado OR #cuarentenatotal) until:2020-09-15 since:2020-08-15"
c.Search = "(#covid) until:2020-09-16 since:2020-08-15"
c.TwitterSearch = True
c.Store_csv = True
c.Limit = 1000
c.Hide_output = True

#c.Lang = "es"
#c.Since = "2020-08-15"
#c.Until = "2020-09-11"
c.Output = "data2.csv"
c.Geo = "4.612639,-74.0705,100km"


# Run
twint.run.Search(c) """

import re

def cleanHash(hashtag: str):
    hashtag = re.sub("[-_#]"," ", hashtag)
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

a = ["Indignante lo que pasa en nuestro país #covid19, asesinan a niños, jóvenes, líderes. Las balas están matando más que el covid, pero indigna aún más ver qué a nadie parece importarle #JusticiaParaLlanoVerde #QuienLosMato", "#ManizalesEnVivo Pará tu bienestar y cuidado Confa lleva el médico hasta tu casa #TeCuidoMeCuidas #QuedateEnCasa #contigocontodo en Manizales, Caldas  https://t.co/o71a8uSqhV"]

for tweet in a:
    print(cleanTweet(tweet))