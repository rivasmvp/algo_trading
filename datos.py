import yfinance as yf
import scraping
import time

inicio = time.perf_counter() #Contador de tiempo de ejecución
def obtener_tickers():
    
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
        
    return(data_1d,data_60m,data_7d)   

# Consulta especifica para descargar los datos del VIX, usado en el índice de volatilidad.

def obtener_vix():
    inicio = time.perf_counter()
    vix_60m = yf.download("^VIX", period="2mo", interval="60m", progress=False)
    vix_1d = yf.download("^VIX", period="2mo", interval="1d", progress=False)
    vix_7d = yf.download("^VIX", period="1y", interval="1wk", progress=False)
    fin = time.perf_counter()
    
    print(f"Datos del VIX descargados en {fin - inicio:.2f} segundos.")
    
    return vix_60m, vix_1d, vix_7d