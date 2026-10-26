# algo_trading - Análisis de mercado con Python.

## NO ES RECOMENDACION DE INVERSIÓN: Usá el engine bajo tu responsabilidad financiera, desalentamos su uso sin experiencia. Perder el 100% del capital es una posibilidad estadística en el mundo de las inversiones.


## Propósito general:
### Escanea el mercado bajo parametros de análisis fundamental de empresas y análisis técnico del precio. 

Análisis fundamental inspirado en el economista estadounidense Benjamin Graham autor de El Inversor Inteligente.

Estrategia de trading inspirada en la triple pantalla de Alexander Elder, extraida de su libro El Nuevo Vivir del Trading. 
 
## - Tickers analizados: Todos los del SP500 junto con su índice, índice NASDAQ, todos los índices sectoriales, Bitcoin, oro y la plata.

## - Stack de análisis técnico: Indicador RSI, indicador MACD, medias móviles y medias moviles ponderadas, accion del precio, soportes y resistencias. Utiliza el índice VIX con umbrales de riesgo.

## - Stack de análisis fundamental de empresas: Fórmula de Graham, EarningsPShare, Free Cash Flow, Payout Ratio, Total Cash, Total Debt, Dividend Rate y Dividend Yield.

# Arquitectura del Sistema: 

## 1.scraping.py -> 2.datos.py -> 3.fundamentales.ipynb -> 4.scanner.py

1.scraping.py: Escaneo simple para no hardcodear una lista de tickers. Se aprovecha para adicionar tickers de interes como los sectoriales.

2.datos.py: Datos cortesía de yfinance. Suelen ser muy fieles y son funcionales a la metodología cuantitativa. Descarga los datos del scraping en la temporalidad por default de 60 minutos, 1 dia y 7 dias.

3.fundamentales.ipynb: Filtra aspectos contables de la empresa con formula de crecimiento.

4.scanner.ipynb: Filtra las empresas sólidas para encontrar sobreventa en su indicador RSI o si el precio se acerca a la EMA150. Además, grafica el índicador de pánico en el mercado por sus umbrales. Marca como posible entrada un activo cuya linea MACD superó a su linea signal.





