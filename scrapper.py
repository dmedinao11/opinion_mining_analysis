import twint
from searchParams import SEARCH_TERMS, genDatesInterval, DateStr, SEARCH_TEMPLATE, SEARCH_TERMS_LIST
from datetime import datetime


#Utilidades
def setUpConfig(query:DateStr, term: str):
    c = twint.Config()
    c.Store_csv = True
    c.Limit = 4000
    c.TwitterSearch = True
    c.Geo = "4.612639,-74.0705,100km"
    c.Output = "output.csv"
    c.Search = SEARCH_TEMPLATE.format(since=query.initDate, until=query.endDate, term=term)
    c.Hide_output = True
    return c



# Generando intervalo
initDate = datetime(2020,8,15)
endDate = datetime(2020,9,16)
datesToResearch = genDatesInterval(initDate, endDate) 
#=========================================================

#Iniciando
for query in datesToResearch:
    for term in SEARCH_TERMS_LIST:
        c = setUpConfig(query, term)
        try:
            twint.run.Search(c)
        except:
            continue
#=========================================================

print("Finished")