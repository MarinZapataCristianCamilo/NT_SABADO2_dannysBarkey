from utils.simularUsuarios import simular_usuarios
from notebook.limpieza import limpiarDatos
import pandas as pd

# Mostrar todas las columnas sin truncar
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

usuarios=simular_usuarios(100)

simulaciones_ordenadas=pd.DataFrame(usuarios)

simulaciones_limpias=limpiarDatos(simulaciones_ordenadas)

print("Datos limpios:")
print(simulaciones_limpias)
print("\nTipos de datos:")
print(simulaciones_limpias.dtypes)





##simulaciones_ordenadas.to_json("data/usuarios.json",orient="records",indent=4)
##
##simulaciones_ordenadas.to_csv("data/usuarios.csv")

