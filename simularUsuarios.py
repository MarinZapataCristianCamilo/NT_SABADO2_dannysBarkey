import random;

def simular_usuarios(num_usuarios):
    usuarios = []
    for i in range(num_usuarios):
        usuario = {
            'id': i,
            'nombre': f'Usuario_{i}',
            'email': f'usuario_{i}@example.com'
        }
        usuarios.append(usuario)
    return usuarios

# Simular la creación de 10 usuarios

usuarios_simulados = simular_usuarios(10)
for usuario in usuarios_simulados:
    print(usuario)
    