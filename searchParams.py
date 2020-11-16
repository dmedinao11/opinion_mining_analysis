from datetime import datetime, timedelta

class DateStr:
    def __init__(self, initDate: datetime, endDate: datetime):
        self.fileName: str = initDate.strftime("%Y-%m-%d.csv")
        self.initDate: str = initDate.strftime("%Y-%m-%d")
        self.endDate: str = endDate.strftime("%Y-%m-%d")


def genDatesInterval(initDate: datetime, endDate: datetime):
    dates = []
    while initDate <= endDate:
        dates.append(DateStr(initDate, initDate + timedelta(days=1)))
        initDate += timedelta(days=2)
    return dates


SEARCH_TERMS = "(# OR #VacunaCOVID19 OR #nomascuarentena OR #wuhan OR #todovaaestarbien OR #BogotaACieloAbierto OR #COVID_19 OR #SARS_CoV_2 OR #vacuna OR #coronavirus OR #YoMeCuidoYoTeCuido OR #infectados OR #cuarentena OR #quedateencasa OR #JuntosEnLaPrevencion OR #autocuidado OR #cuarentenatotal) until:{until} since:{since}"

SEARCH_TERMS_1 = """
    #nomascuarentena
    #wuhan
    #todovaaestarbien 
    #BogotaACieloAbierto  
    #COVID_19 
    #SARS_CoV_2 
    #vacuna 
    #coronavirus 
    #YoMeCuidoYoTeCuido
    #infectados
    #cuarentena
    #quedateencasa
    #JuntosEnLaPrevencion
    #autocuidado
    #cuarentenatotal    
    cuarentena
    wuhan 
    contagios 
    contagio 
    vacuna 
    coronavirus 
    pandemia 
    rebrote 
    confinamiento 
    oms
    tapabocas 
    infectados 
    reactivación económica 
    confinar 
    confinamiento 
    aislamiento 
    distanciamiento
    @pfizer 
    @OPSOMS_Col
    @MinSaludCol
    @SectorSalud
"""