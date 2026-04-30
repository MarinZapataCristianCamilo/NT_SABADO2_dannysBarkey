import os
import pandas as pd


def _asegurar_directorio(ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)


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


def exportar_usuarios(df, carpeta="data"):
    ruta_csv = os.path.join(carpeta, "usuarios.csv")
    ruta_json = os.path.join(carpeta, "usuarios.json")
    _asegurar_directorio(ruta_csv)
    df.to_csv(ruta_csv, index=False)
    df.to_json(ruta_json, orient="records", indent=4, force_ascii=False)
    return ruta_csv, ruta_json


def filtrar_usuarios(df):
    return {
        "usuarios_robert": df.query('usu_nombre == "robert"'),
        "usuarios_id_mayor_500": df.query('usu_id > 500'),
        "usuarios_codigo_an01_an02": df.query('usu_codigo in ["AN01", "AN02"]'),
    }


def agrupar_usuarios(df):
    return (
        df.groupby("usu_nombre", observed=True)
        .agg(
            cantidad_usuarios=pd.NamedAgg(column="usu_id", aggfunc="count"),
            id_promedio=pd.NamedAgg(column="usu_id", aggfunc="mean"),
        )
        .reset_index()
    )


def exportar_productos(df, carpeta="data"):
    ruta_csv = os.path.join(carpeta, "productos.csv")
    ruta_json = os.path.join(carpeta, "productos.json")
    _asegurar_directorio(ruta_csv)
    df.to_csv(ruta_csv, index=False)
    df.to_json(ruta_json, orient="records", indent=4, force_ascii=False)
    return ruta_csv, ruta_json


def filtrar_productos(df):
    return {
        "productos_caros": df.query('pro_precio > 1800'),
        "productos_stock_alto": df.query('pro_stock >= 30'),
        "productos_codigo_an03": df.query('pro_codigo == "AN03"'),
    }


def agrupar_productos(df):
    return (
        df.groupby("pro_nombre", observed=True)
        .agg(
            variantes=pd.NamedAgg(column="pro_codigo", aggfunc="nunique"),
            stock_total=pd.NamedAgg(column="pro_stock", aggfunc="sum"),
            precio_promedio=pd.NamedAgg(column="pro_precio", aggfunc="mean"),
        )
        .reset_index()
    )


def exportar_empleados(df, carpeta="data"):
    ruta_csv = os.path.join(carpeta, "empleados.csv")
    ruta_json = os.path.join(carpeta, "empleados.json")
    _asegurar_directorio(ruta_csv)
    df.to_csv(ruta_csv, index=False)
    df.to_json(ruta_json, orient="records", indent=4, force_ascii=False)
    return ruta_csv, ruta_json


def filtrar_empleados(df):
    return {
        "empleados_salario_alto": df.query('emp_salario > 2500'),
        "empleados_panadero": df.query('emp_cargo == "panadero"'),
        "empleados_codigo_positivos": df.query('emp_codigo >= 1001'),
    }


def agrupar_empleados(df):
    return (
        df.groupby("emp_cargo", observed=True)
        .agg(
            empleados=pd.NamedAgg(column="emp_codigo", aggfunc="count"),
            salario_promedio=pd.NamedAgg(column="emp_salario", aggfunc="mean"),
            salario_total=pd.NamedAgg(column="emp_salario", aggfunc="sum"),
        )
        .reset_index()
    )


def limpiar_ventas(dataFrameSucio):
    dataFrameLimpio = dataFrameSucio.copy()

    dataFrameLimpio["ven_fecha"] = pd.to_datetime(dataFrameLimpio["ven_fecha"], errors="coerce")
    dataFrameLimpio["ven_total"] = pd.to_numeric(dataFrameLimpio["ven_total"], errors="coerce")
    dataFrameLimpio["usu_codigo"] = dataFrameLimpio["usu_codigo"].astype("string").str.strip().str.upper()
    dataFrameLimpio["emp_codigo"] = pd.to_numeric(dataFrameLimpio["emp_codigo"], errors="coerce")

    dataFrameLimpio = dataFrameLimpio[(dataFrameLimpio["ven_total"] > 0) & (dataFrameLimpio["ven_fecha"].notna()) & (dataFrameLimpio["emp_codigo"] > 0)]
    dataFrameLimpio = dataFrameLimpio[dataFrameLimpio["usu_codigo"].isin([codigo.upper() for codigo in ["AN01", "AN02", "AN03", "AN04", "AN05"]])]

    columnas_obligatorias = ["ven_codigo", "ven_fecha", "ven_total", "usu_codigo", "emp_codigo"]
    dataFrameLimpio = dataFrameLimpio.dropna(subset=columnas_obligatorias)
    dataFrameLimpio = dataFrameLimpio.drop_duplicates()
    dataFrameLimpio = dataFrameLimpio[["ven_codigo", "ven_fecha", "ven_total", "usu_codigo", "emp_codigo"]]

    return dataFrameLimpio


def exportar_ventas(df, carpeta="data"):
    ruta_csv = os.path.join(carpeta, "ventas.csv")
    ruta_json = os.path.join(carpeta, "ventas.json")
    _asegurar_directorio(ruta_csv)
    df.to_csv(ruta_csv, index=False)
    df.to_json(ruta_json, orient="records", indent=4, force_ascii=False)
    return ruta_csv, ruta_json


def filtrar_ventas(df):
    fecha_corte = pd.Timestamp.now() - pd.Timedelta(days=180)
    return {
        "ventas_mayores_2500": df.query('ven_total > 2500'),
        "ventas_ultimo_semestre": df.query('ven_fecha >= @fecha_corte'),
        "ventas_por_cliente_an01": df.query('usu_codigo == "AN01"'),
    }


def agrupar_ventas(df):
    resumen_por_empleado = (
        df.groupby("emp_codigo", observed=True)
        .agg(
            ventas_total=pd.NamedAgg(column="ven_total", aggfunc="sum"),
            ventas_count=pd.NamedAgg(column="ven_codigo", aggfunc="count"),
            venta_promedio=pd.NamedAgg(column="ven_total", aggfunc="mean"),
        )
        .reset_index()
    )
    resumen_por_cliente = (
        df.groupby("usu_codigo", observed=True)
        .agg(
            ventas_total=pd.NamedAgg(column="ven_total", aggfunc="sum"),
            ventas_count=pd.NamedAgg(column="ven_codigo", aggfunc="count"),
        )
        .reset_index()
    )
    return {"por_empleado": resumen_por_empleado, "por_cliente": resumen_por_cliente}


