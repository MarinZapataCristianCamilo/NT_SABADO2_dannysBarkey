from utils.simularUsuarios import simular_usuarios
from utils.simularProductos import simular_productos
from utils.simularEmpleados import simular_empleados

from notebook.limpieza import (
    limpiarDatos,
    limpiar_productos,
    limpiar_empleados,
    exportar_usuarios,
    exportar_productos,
    exportar_empleados,
    filtrar_usuarios,
    filtrar_productos,
    filtrar_empleados,
    agrupar_usuarios,
    agrupar_productos,
    agrupar_empleados
)
from utils.simularVentas import simular_ventas

from notebook.limpieza import (
    limpiar_ventas,
    exportar_ventas,
    filtrar_ventas,
    agrupar_ventas
)

from notebook.descripcion import analizar_ventas

from notebook.descripcion import (
    describirDatosProductos,
    describirDatosUsuario,
    describirDatosEmpleados
)
import os
import pandas as pd

# =========================
# CONFIGURACIÓN VISUAL
# =========================
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', 20)

# =========================
# SIMULACIÓN 
# =========================
usuarios = simular_usuarios(1000)
productos = simular_productos(1000)
empleados = simular_empleados(1000)
ventas = simular_ventas(1000)

simulaciones_ventas = pd.DataFrame(ventas)
simulaciones_usuarios = pd.DataFrame(usuarios)
simulaciones_productos = pd.DataFrame(productos)
simulaciones_empleados = pd.DataFrame(empleados)

# =========================
# LIMPIEZA 
# =========================
simulacionesLimpiasUsuarios = limpiarDatos(simulaciones_usuarios)
simulacionesLimpiasProductos = limpiar_productos(simulaciones_productos)
simulacionesLimpiasEmpleado = limpiar_empleados(simulaciones_empleados)
simulacionesLimpiasVentas = limpiar_ventas(simulaciones_ventas)

print("\n=========== DATOS LIMPIOS (MUESTRA) ===========")

print("\nUsuarios:")
print(simulacionesLimpiasUsuarios.head())

print("\nProductos:")
print(simulacionesLimpiasProductos.head())

print("\nEmpleados:")
print(simulacionesLimpiasEmpleado.head())

print("\nVentas:")
print(simulacionesLimpiasVentas.head())

print("\n================================================")

# =========================
# DESCRIPCIÓN
# =========================
print("\n=========== DESCRIPCIÓN USUARIOS ===========")
describirDatosUsuario(simulacionesLimpiasUsuarios)

print("\n=========== DESCRIPCIÓN PRODUCTOS ===========")
describirDatosProductos(simulacionesLimpiasProductos)

print("\n=========== DESCRIPCIÓN EMPLEADOS ===========")
describirDatosEmpleados(simulacionesLimpiasEmpleado)

# =========================
# FILTROS 
# =========================
print("\n=========== FILTROS ===========")

filtros_usuarios = filtrar_usuarios(simulacionesLimpiasUsuarios)
for nombre, df in filtros_usuarios.items():
    print(f"\nFiltro usuarios: {nombre}")
    print(df.head())

filtros_productos = filtrar_productos(simulacionesLimpiasProductos)
for nombre, df in filtros_productos.items():
    print(f"\nFiltro productos: {nombre}")
    print(df.head())

filtros_empleados = filtrar_empleados(simulacionesLimpiasEmpleado)
for nombre, df in filtros_empleados.items():
    print(f"\nFiltro empleados: {nombre}")
    print(df.head())

filtros_ventas = filtrar_ventas(simulacionesLimpiasVentas)

for nombre, df in filtros_ventas.items():
    print(f"\nFiltro ventas: {nombre}")
    print(df.head())

# =========================
# AGRUPACIONES
# =========================
print("\n=========== AGRUPACIONES ===========")

print("\nUsuarios agrupados:")
print(agrupar_usuarios(simulacionesLimpiasUsuarios))

print("\nProductos agrupados:")
print(agrupar_productos(simulacionesLimpiasProductos))

print("\nEmpleados agrupados:")
print(agrupar_empleados(simulacionesLimpiasEmpleado))

print("\nVentas agrupadas:")
agrupaciones_ventas = agrupar_ventas(simulacionesLimpiasVentas)

print("\nPor empleado:")
print(agrupaciones_ventas["por_empleado"])

print("\nPor cliente:")
print(agrupaciones_ventas["por_cliente"])

# =========================
#  EXPORTACIÓN 
# =========================
print("\n=========== EXPORTANDO DATOS ===========")

ruta_usuarios = exportar_usuarios(simulacionesLimpiasUsuarios)
print(f"Usuarios exportados en: {ruta_usuarios}")

ruta_productos = exportar_productos(simulacionesLimpiasProductos)
print(f"Productos exportados en: {ruta_productos}")

ruta_empleados = exportar_empleados(simulacionesLimpiasEmpleado)
print(f"Empleados exportados en: {ruta_empleados}")

ruta_ventas = exportar_ventas(simulacionesLimpiasVentas)
print(f"Ventas exportadas en: {ruta_ventas}")

print("Ruta actual:", os.getcwd())

# =========================
#  VALIDACIÓN 
# =========================
print("\n=========== VALIDACIÓN DE ARCHIVOS ===========")

df_test_csv = pd.read_csv("data/usuarios.csv")
print("CSV usuarios OK:", df_test_csv.shape)

df_test_json = pd.read_json("data/usuarios.json")
print("JSON usuarios OK:", df_test_json.shape)