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
    print("=== descripcion del dataset de usuarios ===")
    print(f"\nnumero de filas del dataset: {dataFrameLimpio.shape[0]}")
    print(f"\nnumero de columnas del dataset: {dataFrameLimpio.shape[1]}")
    print(f"\nlista de columnas disponibles: {list(dataFrameLimpio.columns)}")
    print(f"\ntipo de datos de cada atributo:\n{dataFrameLimpio.dtypes}")

    print("***estadisticas***")
    print(dataFrameLimpio.describe(include="all"))

    print("***conteos***")
    if "usu_codigo" in dataFrameLimpio.columns:
        print(dataFrameLimpio["usu_codigo"].value_counts())


def describirDatosProductos(dataFrameLimpio):
    print("=== descripcion del dataset de productos ===")
    print(f"\nnumero de filas del dataset: {dataFrameLimpio.shape[0]}")
    print(f"\nnumero de columnas del dataset: {dataFrameLimpio.shape[1]}")
    print(f"\nlista de columnas disponibles: {list(dataFrameLimpio.columns)}")
    print(f"\ntipo de datos de cada atributo:\n{dataFrameLimpio.dtypes}")

    print("***estadisticas***")
    print(dataFrameLimpio[["pro_precio", "pro_stock"]].describe())

    print("***conteos***")
    if "pro_stock" in dataFrameLimpio.columns:
        print(dataFrameLimpio["pro_stock"].value_counts())
    if "pro_codigo" in dataFrameLimpio.columns:
        print(dataFrameLimpio["pro_codigo"].value_counts())


def analizar_empleados(dataFrameLimpio):
    print("=== descripcion del dataset de empleados ===")
    print(f"\nnumero de filas del dataset: {dataFrameLimpio.shape[0]}")
    print(f"\nnumero de columnas del dataset: {dataFrameLimpio.shape[1]}")
    print(f"\nlista de columnas disponibles: {list(dataFrameLimpio.columns)}")
    print(f"\ntipo de datos de cada atributo:\n{dataFrameLimpio.dtypes}")

    print("***estadisticas***")
    print(dataFrameLimpio.describe(include="all"))

    print("***conteos***")
    if "emp_cargo" in dataFrameLimpio.columns:
        print(dataFrameLimpio["emp_cargo"].value_counts())


def analizar_ventas(dataFrameLimpio):
    print("=== descripcion del dataset de ventas ===")
    print(f"\nnumero de filas del dataset: {dataFrameLimpio.shape[0]}")
    print(f"\nnumero de columnas del dataset: {dataFrameLimpio.shape[1]}")
    print(f"\nlista de columnas disponibles: {list(dataFrameLimpio.columns)}")
    print(f"\ntipo de datos de cada atributo:\n{dataFrameLimpio.dtypes}")

    print("***estadisticas***")
    print(dataFrameLimpio.describe(include="all"))

    print("***conteos***")
    if "usu_codigo" in dataFrameLimpio.columns:
        print(dataFrameLimpio["usu_codigo"].value_counts())

    
    if "ven_fecha" in dataFrameLimpio.columns:
        print("***rango de fechas***")
        print("fecha minima:", dataFrameLimpio["ven_fecha"].min())
        print("fecha maxima:", dataFrameLimpio["ven_fecha"].max())

def describirDatosEmpleados(dataFrameLimpio):
    print("=== descripcion del dataset de empleados ===")
    print(f"\nnumero de filas del dataset: {dataFrameLimpio.shape[0]}")
    print(f"\nnumero de columnas del dataset: {dataFrameLimpio.shape[1]}")
    print(f"\nlista de columnas disponibles: {list(dataFrameLimpio.columns)}")
    print(f"\ntipo de datos de cada atributo:\n{dataFrameLimpio.dtypes}")

    print("***estadisticas***")
    # columna numerica real en tu modelo
    if "emp_salario" in dataFrameLimpio.columns:
        print(dataFrameLimpio[["emp_salario"]].describe())
    else:
        print(dataFrameLimpio.describe(include="all"))

    print("***conteos***")
    if "emp_cargo" in dataFrameLimpio.columns:
        print("\nconteo por cargo:")
        print(dataFrameLimpio["emp_cargo"].value_counts())

    if "emp_nombre" in dataFrameLimpio.columns:
        print("\nconteo por nombre:")
        print(dataFrameLimpio["emp_nombre"].value_counts())

    if "emp_codigo" in dataFrameLimpio.columns:
        print("\nconteo por codigo:")
        print(dataFrameLimpio["emp_codigo"].value_counts())
