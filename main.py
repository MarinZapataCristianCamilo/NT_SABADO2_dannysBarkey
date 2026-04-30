from utils.simularUsuarios import simular_usuarios
from utils.simularProductos import simular_productos
from utils.simularEmpleados import simular_empleados
from notebook.limpieza import limpiarDatos, limpiar_productos, limpiar_empleados
from notebook.descripcion import describirDatosProductos, describirDatosUsuario, describirDatosEmpleados
import pandas as pd

# Mostrar todas las columnas sin truncar
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

usuarios = simular_usuarios(1000)
productos = simular_productos(1000)
empleados = simular_empleados(1000)

simulaciones_usuarios = pd.DataFrame(usuarios)
simulaciones_productos = pd.DataFrame(productos)
simulaciones_empleados = pd.DataFrame(empleados)

simulacionesLimpiasUsuarios = limpiarDatos(simulaciones_usuarios)
simulacionesLimpiasProductos = limpiar_productos(simulaciones_productos)
simulacionesLimpiasEmpleado = limpiar_empleados(simulaciones_empleados)

print("Mostrando registros limpios de usuarios")
print(simulacionesLimpiasUsuarios)
print("\nMostrando registros limpios de productos")
print(simulacionesLimpiasProductos)
print("\nMostrando registros limpios de empleados")
print(simulacionesLimpiasEmpleado)

print("***********************************************************")


describirDatosUsuario(simulacionesLimpiasUsuarios)
describirDatosProductos(simulacionesLimpiasProductos)
describirDatosEmpleados(simulacionesLimpiasEmpleado)




##simulaciones_ordenadas.to_json("data/usuarios.json",orient="records",indent=4)
##
##simulaciones_ordenadas.to_csv("data/usuarios.csv")

