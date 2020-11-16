import twint
from searchParams import SEARCH_TERMS, genDatesInterval, DateStr
from datetime import datetime


#Utilidades
def setUpConfig(query:DateStr):
    c = twint.Config()
    c.Store_csv = True
    c.Limit = 1500
    c.Geo = "4.612639,-74.0705,30km"
    c.Output = query.fileName
    c.Search = SEARCH_TERMS.format(since=query.initDate, until=query.endDate)
    return c


def scrappe(queryList):
    if len(queryList) == 0:
        return None
    else:
        query = queryList.pop()
        c = setUpConfig(query)
        

        def callbackFunction(args):
            twint.run.Search(c, scrappe(queryList))

        return callbackFunction
    

# Generando intervalo
initDate = datetime(2020,8,15)
endDate = datetime(2020,9,16)
datesToResearch = genDatesInterval(initDate, endDate) 
#=========================================================

#Iniciando
c = setUpConfig(datesToResearch.pop())
#print(c.Until)
twint.run.Search(c, scrappe(datesToResearch))
#=========================================================