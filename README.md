# algo_trading - Análisis de mercado con Python.

> NO ES RECOMENDACION DE INVERSIÓN: Usá el engine bajo tu responsabilidad financiera, desalentamos su uso sin experiencia. Perder el 100% del capital es una posibilidad estadística en el mundo de las inversiones.


## Propósito general:
Escanea el mercado bajo parametros de análisis fundamental de empresas y análisis técnico del precio con un enfoque de 
análisis fundamental inspirado en el economista estadounidense Benjamin Graham autor de El Inversor Inteligente y las
estrategias de trading inspirada en la triple pantalla de Alexander Elder, extraida de su libro El Nuevo Vivir del Trading. 
 
# Arquitectura del Sistema: 

### 1.scraping.py -> 2.datos.py -> 3.fundamentales.ipynb -> 4.scanner.ipynb

1.scraping.py: Hace un web scraping de los tickers del SP500 y su índice, índice NASDAQ, todos los índices sectoriales, Bitcoin, oro y la plata. Además se suman ETF'S sectoriales apalancados.

2.datos.py: Datos cortesía de yfinance. Suelen ser muy fieles y son funcionales a la metodología cuantitativa. Descarga los datos del scraping en la temporalidad por default de 60 minutos, 1 dia y 7 dias.

3.fundamentales.ipynb: Filtra aspectos contables de la empresa con formula de crecimiento de Graham, EarningsPShare, Free Cash Flow, Payout Ratio,  Total Debt, Dividend Rate y Dividend Yield.

4.scanner.ipynb: Filtra las empresas sólidas para encontrar sobreventa en su indicador RSI o si el precio se acerca a la EMA150. Además, grafica el índicador de pánico en el mercado por sus umbrales. indicador MACD, medias móviles y medias moviles ponderadas, accion del precio, soportes y resistencias.




