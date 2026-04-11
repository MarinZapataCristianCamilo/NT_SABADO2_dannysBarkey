from utils.simularUsuarios import simular_usuarios
import pandas as pd


usuarios=simular_usuarios(10)

simulaciones_ordenadas=pd.DataFrame(usuarios)
print(simulaciones_ordenadas)


simulaciones_ordenadas.to_json("data/usuarios.json",orient="records",indent=4)

simulaciones_ordenadas.to_csv("data/usuarios.csv")