#Importa las librerias requeridas.

import pandas as pd
import requests
import io

#Scrapea Wikipedia para acceder a los nombres de los tickers del S&P500.


#1.1 Define la URL y un 'User-Agent' para evitar el bloqueo.
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

#1.2 Realiza la petición con el header de seguridad
r = requests.get(url, headers=header)

#1.3 Lee la tabla desde el texto de la respuesta, usando io.StringIO para forzar la interpretación como string HTML
tables = pd.read_html(io.StringIO(r.text))
df_spy = tables[0]

#1.4 Extrae la lista de Tickers
tickers_a_analizar = [t.replace('.', '-') for t in df_spy['Symbol'].tolist()]

#1.5 Añade tickers de interes.

mis_tickers = ['^VIX', 'SPY', 'SPXL' , 'TQQQ' , 'QQQ' , 'URA' , 'XLI' , 'XLF' , 'XLRE' , 'XLB' , 'XLY' , 'XLE', 'XLV' ,
                'XBI' , 'XLC' , 'BTC-USD' , 'DIA'
                'XLK' , 'SMH', 'XLP', 'XLU', 'CIBR', 'IBB', 'ICLN','ARKK','COPX','GDX'
                ]

tickers_a_analizar.extend(mis_tickers)

if tickers_a_analizar:
  print(f"Se han cargado {len(tickers_a_analizar)} tickers...")