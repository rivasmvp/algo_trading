import yfinance as yf
from web_scraping import obtener_tickers

tickers_limpios = obtener_tickers()

# Descarga de datos temporalidad 60m.

data_60m = yf.download(tickers_limpios, period="2mo", interval="60m", group_by='ticker', progress=False)

# Descarga de datos temporalidad 1d.
data_1d = yf.download(tickers_limpios, period="2mo", interval="1d", group_by='ticker', progress=False)

# Descarga de datos temporalidad 7d.
data_7d = yf.download(tickers_limpios, period="1y", interval="1wk", group_by='ticker', progress=False)