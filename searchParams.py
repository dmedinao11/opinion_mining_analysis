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

SEARCH_TERMS_LIST = [
    "#nomascuarentena",
    "#wuhan",
    "#todovaaestarbien" ,
    "#BogotaACieloAbierto"  ,
    "#COVID_19" ,
    "#SARS_CoV_2" ,
    "#vacuna" ,
    "#coronavirus" ,
    "#YoMeCuidoYoTeCuido",
    "#infectados",
    "#cuarentena",
    "#quedateencasa",
    "#JuntosEnLaPrevencion",
    "#autocuidado",
    "#cuarentenatotal"   ,
    "#gripa",
    "#covid",
    "#covid19",
    "#covid-19",
    "#covid_19",
    "#virus",
    "#uci",
    "#MeCuidoTeCuido",
    "#NoBajemosLaGuardia",
    "#SiNosCuidamosAvanzamos",
    "#contagios" ,
    "#contagio" ,
    "#Moderna",
    "#oms",
    "#infectado",
    "#tapabocas" ,
    "#mascarilla" ,
    "#UnidosNosCuidamos",
    "#pandemia",
    "#distanciamientosocial",
    "#ReporteCOVID19",
    "#nuevarealidad",
    "#tapaboca",
    "#prevencion",
    "#YoMeCuidoYoCuidoAMiFamila",
    "#elvirusnosehaido",
    "prevencion",
    "tapaboca",
    "pcr",
    "distanciamiento social",
    "nueva realidad",
    "mascarilla" ,
    "infectado",
    "vacuna",
    "moderna",
    "vacunas",
    "pfizer",
    "Pfizer",
    "mutación",
    "No Bajemos La Guardia",
    "Me Cuido Te Cuido",
    "uci",
    "covid_19",
    "virus",
    "covid19",
    "covid-19",
    "covid",
    "gripa",
    "cuarentena",
    "wuhan" ,
    "contagios" ,
    "contagio" ,
    "vacuna" ,
    "vacunas" ,
    "coronavirus" ,
    "pandemia" ,
    "rebrote" ,
    "confinamiento" ,
    "oms",
    "tapabocas" ,
    "infectados" ,
    "reactivación económica" ,
    "reactivacion economica" ,
    "confinar" ,
    "confinamiento" ,
    "aislamiento" ,
    "distanciamiento"
]

SEARCH_TEMPLATE = "({term}) until:{until} since:{since}"