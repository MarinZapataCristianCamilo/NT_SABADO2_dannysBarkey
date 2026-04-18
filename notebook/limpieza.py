import pandas as pd

def limpiarDatos(dataFrameSucio):

    #todo dataframe puede copiarse
    dataFrameLimpio = dataFrameSucio.copy()

    #paso 1. limpiar las columnas String del dataframe
    columnas_texto = ["usu_nombre", "usu_email", "usu_codigo"]
    for columna in columnas_texto:
        dataFrameLimpio[columna] = dataFrameLimpio[columna].astype("string").str.strip().str.lower()

    #paso 1.1 definir valores de string esperados
    valoresValidosNombre = ["robert", "adelaida", "mariana", "isabela"]
    dataFrameLimpio["usu_nombre"] = dataFrameLimpio["usu_nombre"].where(
        dataFrameLimpio["usu_nombre"].isin(valoresValidosNombre),
        pd.NA
    )
    
    valoresValidosEmail = ["robert@example.com", "adelaida@example.com", "mariana@example.com", "isabela@example.com"]
    dataFrameLimpio["usu_email"] = dataFrameLimpio["usu_email"].where(
        dataFrameLimpio["usu_email"].isin(valoresValidosEmail),
        pd.NA
    )
    
    valoresValidosCodigo = ["an01", "an02", "an03", "an04", "an05"]
    dataFrameLimpio["usu_codigo"] = dataFrameLimpio["usu_codigo"].where(
        dataFrameLimpio["usu_codigo"].isin(valoresValidosCodigo),
        pd.NA
    )

    #paso 2. limpiar las columnas numericas del dataframe
    dataFrameLimpio["usu_id"] = pd.to_numeric(dataFrameLimpio["usu_id"], errors='coerce')

    #paso 2.1 limpiando campos numericos que no tengan valores validos
    dataFrameLimpio = dataFrameLimpio[dataFrameLimpio["usu_id"] > 0]

    #paso 4. eliminar registros que tengan datos obligatorios vacios
    columnas_obligatorias = ["usu_id", "usu_nombre", "usu_email", "usu_codigo"]
    dataFrameLimpio = dataFrameLimpio.dropna(subset=columnas_obligatorias)

    #paso 5. eliminar registros duplicados
    dataFrameLimpio = dataFrameLimpio.drop_duplicates()
    
    # Reordenar columnas: usu_id, usu_nombre, usu_email, usu_codigo
    dataFrameLimpio = dataFrameLimpio[["usu_id", "usu_nombre", "usu_email", "usu_codigo"]]
    
    return dataFrameLimpio





