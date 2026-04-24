import pandas as pd


def limpiarDatos(dataFrameSucio):
    return limpiar_usuarios(dataFrameSucio)


def limpiar_usuarios(dataFrameSucio):
    dataFrameLimpio = dataFrameSucio.copy()

    columnas_texto = ["usu_nombre", "usu_email", "usu_codigo"]
    for columna in columnas_texto:
        dataFrameLimpio[columna] = dataFrameLimpio[columna].astype("string").str.strip().str.lower()

    valoresValidosNombre = ["robert", "adelaida", "mariana", "isabela"]
    dataFrameLimpio["usu_nombre"] = dataFrameLimpio["usu_nombre"].where(
        dataFrameLimpio["usu_nombre"].isin(valoresValidosNombre),
        pd.NA
    )

    valoresValidosEmail = [f"{nombre}@example.com" for nombre in valoresValidosNombre]
    dataFrameLimpio["usu_email"] = dataFrameLimpio["usu_email"].where(
        dataFrameLimpio["usu_email"].isin(valoresValidosEmail),
        pd.NA
    )

    valoresValidosCodigo = ["an01", "an02", "an03", "an04", "an05"]
    dataFrameLimpio["usu_codigo"] = dataFrameLimpio["usu_codigo"].where(
        dataFrameLimpio["usu_codigo"].isin(valoresValidosCodigo),
        pd.NA
    )

    dataFrameLimpio["usu_id"] = pd.to_numeric(dataFrameLimpio["usu_id"], errors="coerce")
    dataFrameLimpio = dataFrameLimpio[dataFrameLimpio["usu_id"] > 0]

    columnas_obligatorias = ["usu_id", "usu_nombre", "usu_email", "usu_codigo"]
    dataFrameLimpio = dataFrameLimpio.dropna(subset=columnas_obligatorias)
    dataFrameLimpio = dataFrameLimpio.drop_duplicates()
    dataFrameLimpio = dataFrameLimpio[["usu_id", "usu_nombre", "usu_email", "usu_codigo"]]

    return dataFrameLimpio


def limpiar_productos(dataFrameSucio):
    dataFrameLimpio = dataFrameSucio.copy()

    columnas_texto = ["pro_nombre", "pro_codigo"]
    for columna in columnas_texto:
        dataFrameLimpio[columna] = dataFrameLimpio[columna].astype("string").str.strip().str.lower()

    valoresValidosNombre = ["pan", "pastel", "galleta", "croissant"]
    valoresValidosCodigo = ["an01", "an02", "an03", "an04", "an05"]

    dataFrameLimpio["pro_nombre"] = dataFrameLimpio["pro_nombre"].where(
        dataFrameLimpio["pro_nombre"].isin(valoresValidosNombre),
        pd.NA
    )
    dataFrameLimpio["pro_codigo"] = dataFrameLimpio["pro_codigo"].where(
        dataFrameLimpio["pro_codigo"].isin(valoresValidosCodigo),
        pd.NA
    )

    dataFrameLimpio["pro_precio"] = pd.to_numeric(dataFrameLimpio["pro_precio"], errors="coerce")
    dataFrameLimpio["pro_stock"] = pd.to_numeric(dataFrameLimpio["pro_stock"], errors="coerce")

    dataFrameLimpio = dataFrameLimpio[(dataFrameLimpio["pro_precio"] > 0) & (dataFrameLimpio["pro_stock"] >= 0)]

    columnas_obligatorias = ["pro_nombre", "pro_precio", "pro_codigo", "pro_stock"]
    dataFrameLimpio = dataFrameLimpio.dropna(subset=columnas_obligatorias)
    dataFrameLimpio = dataFrameLimpio.drop_duplicates()
    dataFrameLimpio = dataFrameLimpio[["pro_nombre", "pro_precio", "pro_codigo", "pro_stock"]]

    return dataFrameLimpio


def limpiar_empleados(dataFrameSucio):
    dataFrameLimpio = dataFrameSucio.copy()

    columnas_texto = ["emp_nombre", "emp_email", "emp_id", "emp_cargo"]
    for columna in columnas_texto:
        dataFrameLimpio[columna] = dataFrameLimpio[columna].astype("string").str.strip().str.lower()

    valoresValidosNombre = ["robert", "adelaida", "mariana", "isabela"]
    valoresValidosCargo = ["panadero", "pastelero", "vendedor", "administrador"]
    valoresValidosEmail = [f"{nombre}@example.com" for nombre in valoresValidosNombre]

    dataFrameLimpio["emp_nombre"] = dataFrameLimpio["emp_nombre"].where(
        dataFrameLimpio["emp_nombre"].isin(valoresValidosNombre),
        pd.NA
    )
    dataFrameLimpio["emp_email"] = dataFrameLimpio["emp_email"].where(
        dataFrameLimpio["emp_email"].isin(valoresValidosEmail),
        pd.NA
    )
    dataFrameLimpio["emp_cargo"] = dataFrameLimpio["emp_cargo"].where(
        dataFrameLimpio["emp_cargo"].isin(valoresValidosCargo),
        pd.NA
    )

    dataFrameLimpio["emp_id"] = dataFrameLimpio["emp_id"].where(
        dataFrameLimpio["emp_id"].str.len().between(1, 10),
        pd.NA
    )

    dataFrameLimpio["emp_codigo"] = pd.to_numeric(dataFrameLimpio["emp_codigo"], errors="coerce")
    dataFrameLimpio["emp_salario"] = pd.to_numeric(dataFrameLimpio["emp_salario"], errors="coerce")

    dataFrameLimpio = dataFrameLimpio[(dataFrameLimpio["emp_codigo"] > 0) & (dataFrameLimpio["emp_salario"] > 0)]

    columnas_obligatorias = ["emp_codigo", "emp_nombre", "emp_email", "emp_id", "emp_cargo", "emp_salario"]
    dataFrameLimpio = dataFrameLimpio.dropna(subset=columnas_obligatorias)
    dataFrameLimpio = dataFrameLimpio.drop_duplicates()
    dataFrameLimpio = dataFrameLimpio[["emp_codigo", "emp_nombre", "emp_email", "emp_id", "emp_cargo", "emp_salario"]]

    return dataFrameLimpio





