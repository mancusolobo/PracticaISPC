from Investpy import Investpy
from yFinance import yFinance
from Webscraping import Webscraping
from Graficos import Graficos

if __name__ == "__main__":
  
  #Agregamos los datos
  url="https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
  table = {"id":"ctl00_Contenido_tblAcciones"}
  tickers = 'BBVA TELEFONICA B.SANTANDER'
  tickers2 = 'BBVA SAN TEF'

  #Creamos las instancias
  data = Webscraping(url, table, tickers)
  data2 = yFinance(tickers2)
  data3 = Investpy(tickers2)

  #Creamos diccionario con las instancias
  dict_data = dict(zip(['Webscraping', 'Yfinance', 'Investpy'], [data, data2, data3]))

  #Ejecutamos los metodos de las instancias y creamos un diccionario con los dataframes
  dict_df = {}
  for name, data in dict_data.items():
    data.toCSV(name)
    dict_df[name] = data.toDF()
    print('--- {0} ---'.format(name))
    print(data.maximos('Maximo', 1))
    print(data.minimos('Minimo', 1))

  #Generamos los graficos con los dataframes
  graficos = Graficos(dict_df)
  graficos.dibujar(10)