#toda rutina de analizis debe describir el dataset

#1. es importante conocer cuantos registros tengo
#2. es importante conocer cuantos atributos tengo
#3. es util tener acceso a una lista con los nombres de los atributos
#4. es util hacer conteos de algunas columnas de interes
#5. es util conocer las estadisticas descriptivas de los campos numericos
#Media-max-min-std-percentiles
#si hay fechas, es util conocer la fecha mas antigua y la fecha mas reciente
import pandas as pd
def describirDatosUsuario(dataFrameLimpio):
    print("descripcion del dataset*")
    print(f"\nnumero de filas del dataset: {dataFrameLimpio.shape[0]}")
    print(f"\nnumero de columnas del dataset: {dataFrameLimpio.shape[1]}")
    print(f"\nlista de columnas disponibles: {list(dataFrameLimpio.columns)}")
    print(f"\ntipo de datos de cada atributo: {dataFrameLimpio.dtypes}")

    #estadisticas (solo aplica para datos numericos)
    print("***\n" \
    "estadisticas***")
    print(f"{dataFrameLimpio[["usu_id","usu_email",]].describe()}")

    #informacion de conteos valiosos 
    print("***\n" \
    "conteos***")
    print(f"{dataFrameLimpio["usu_codigo"].value_counts()}")

