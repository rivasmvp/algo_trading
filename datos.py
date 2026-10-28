import yfinance as yf
import scraping
import time

inicio = time.perf_counter() #Contador de tiempo de ejecución
def obtener_tickers(temporalidad, periodo):
    
    tickers_limpios = scraping.scrapear_tickers()
    
    # Descarga de datos temporalidad *temporalidad* y el periodo *periodo*.
    data = yf.download(tickers_limpios, period=periodo , interval=temporalidad, group_by='ticker', progress=False)
    
    fin = time.perf_counter() #Contador de tiempo de ejecución
    tiempo_total = fin - inicio #Contador de tiempo de ejecución

    print(f"Tiempo de descarga en {tiempo_total:.2f} segundos.")

    if not data.empty:
        print(f"Se descargó datos en temporalidad{temporalidad} con un periodo de {periodo}")
        
    return(data)   

# Consulta especifica para descargar los datos del VIX, usado en el índice de volatilidad.

def obtener_vix():
    inicio = time.perf_counter()
    vix_60m = yf.download("^VIX", period="2mo", interval="60m", progress=False)
    vix_1d = yf.download("^VIX", period="2mo", interval="1d", progress=False)
    vix_7d = yf.download("^VIX", period="1y", interval="1wk", progress=False)
    fin = time.perf_counter()
    
    print(f"Datos del VIX descargados en {fin - inicio:.2f} segundos.")
    
    return vix_60m, vix_1d, vix_7d