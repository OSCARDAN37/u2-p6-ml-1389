import pandas as pd
import numpy as np
# Oscar  Flores Nc = 1389
serie_amigos =["Pedro", "Morgan", "Farfan", "Adrian", "Jesse", "Oscar", "Mario"]
print("-- Serie listado de amigos NC = 1389 --")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes =[20,50,100,200,500,1000]
print("-- Serie listado de billetes MX NC = 1389 --")
billetes = pd.Series(serie_billetes)
print(billetes)

serie_billetes =[20,50,100,200,500,1000]
serie_bletras =["vente","cincuenta","cien","doscientos","quinientos","mil"]
print("-- Serie listado nombre y valor de billetes MX NC = 1389 --")
tablabilletes = pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)
# Diccionario dataframe
# Diccionario de valor mobedas y nombre
print("-- Datos de diccionario a DataFrame en pandas NC = 1389 --")
dic_monedas = {
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras" :["vente","cincuenta","cien","doscientos","quinientos","mil"]

}
tablabilletes = pd.DataFrame(dic_monedas, index = ["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Oscar Flores NC = 1389")