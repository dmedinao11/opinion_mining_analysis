# Configure
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
twint.run.Search(c)