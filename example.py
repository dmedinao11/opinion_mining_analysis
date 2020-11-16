# Configure
import twint


c = twint.Config()
#c.Search = "(# OR #nomascuarentena OR #wuhan OR #todovaaestarbien OR #BogotaACieloAbierto OR #COVID_19 OR #SARS_CoV_2 OR #vacuna OR #coronavirus OR #YoMeCuidoYoTeCuido OR #infectados OR #cuarentena OR #quedateencasa OR #JuntosEnLaPrevencion OR #autocuidado OR #cuarentenatotal) until:2020-09-15 since:2020-08-15"
c.Search = "(cuarentena OR wuhan OR contagios OR contagio OR vacuna OR coronavirus OR pandemia OR rebrote OR confinamiento OR oms OR tapabocas OR infectados OR reactivación OR económica OR confinar OR confinamiento OR aislamiento OR distanciamiento) until:2020-09-15 since:2020-08-15"
c.TwitterSearch = True
c.Store_csv = True
c.Limit = 200
#c.Lang = "es"
#c.Since = "2020-08-15"
#c.Until = "2020-09-11"
c.Output = "data.csv"
c.Geo = "4.612639,-74.0705,30km"
c.Filter_retweets = True


# Run
twint.run.Search(c)