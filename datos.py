import yfinance as yf
import scraping
import time

inicio = time.perf_counter() #Contador de tiempo de ejecución

tickers_limpios = scraping.obtener_tickers()

# Descarga de datos temporalidad 60m.

data_60m = yf.download(tickers_limpios, period="2mo", interval="60m", group_by='ticker', progress=False)

# Descarga de datos temporalidad 1d.
data_1d = yf.download(tickers_limpios, period="2mo", interval="1d", group_by='ticker', progress=False)

# Descarga de datos temporalidad 7d.
data_7d = yf.download(tickers_limpios, period="1y", interval="1wk", group_by='ticker', progress=False)

fin = time.perf_counter() #Contador de tiempo de ejecución
tiempo_total = fin - inicio #Contador de tiempo de ejecución

print(f"Tiempo de descarga en {tiempo_total:.2f} segundos.")

if not data_60m.empty and not data_1d.empty and not data_7d.empty:
    print("Se descargó todas las temporalidades")