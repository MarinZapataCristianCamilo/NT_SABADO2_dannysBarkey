import random


def simular_usuarios(numeroUsuarios):
    listaUsuarios = ["robert", "adelaida", "mariana", "isabela"]
    listaCodigos = ["AN01", "AN02", "AN03", "AN04", "AN05"]

    usuarios = []

    for _ in range(numeroUsuarios):
        nombre = random.choice(listaUsuarios)
        usuario = {
            "usu_codigo": random.choice(listaCodigos),
            "usu_nombre": nombre,
            "usu_email": f"{nombre}@example.com",
            "usu_id": random.randint(1, 5000)
        }

        probabilidad_error = random.random()
        if probabilidad_error < 0.15:
            usuario["usu_codigo"] = random.choice([None, "AN99", "  ", "-1"])
        elif probabilidad_error < 0.35:
            usuario["usu_id"] = random.choice([None, -1, 0, "abc", " "])
        elif probabilidad_error < 0.6:
            usuario["usu_email"] = random.choice([None, "NaN", "invalid_email", " RObert@example.com ", "robert@invalid"])
        elif probabilidad_error < 0.85:
            usuario["usu_nombre"] = random.choice([None, "NaN", "", "   ", "juan"])

        usuarios.append(usuario)

    return usuarios

