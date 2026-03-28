import random

def simular_usuarios(numeroUsuarios):
    
    listaUsuarios = ["robert", "adelaida", "mariana", "isabela"]

    listaEmails = ["robert@example.com", "adelaida@example.com", "mariana@example.com", "isabela@example.com"]

    listaCodigos = ["AN01", "AN02", "AN03", "AN04", "AN05"]

    usuarios=[]

    for _ in range(numeroUsuarios):

        usuario={
            "usu_codigo":random.randint(0, 5000),
            "usu_nombre":random.choice(listaUsuarios),
            "usu_email":random.choice(listaEmails),
            "usu_id":random.randint(0, 5000)
        }
        usuarios.append(usuario)
    return usuarios

