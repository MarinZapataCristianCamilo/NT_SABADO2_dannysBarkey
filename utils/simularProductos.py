import random

# panaderia dannysBarkey

def simular_productos(numeroProductos):
    pro_nombres = ["pan", "pastel", "galleta", "croissant"]
    pro_precios = [1500, 2500, 500, 2000]
    pro_codigos = ["AN01", "AN02", "AN03", "AN04", "AN05"]
    pro_stock = [10, 20, 30, 40, 50]

    productos = []

    for _ in range(numeroProductos):
        nombre = random.choice(pro_nombres)
        producto = {
            "pro_nombre": nombre,
            "pro_precio": random.choice(pro_precios),
            "pro_codigo": random.choice(pro_codigos),
            "pro_stock": random.choice(pro_stock)
        }

        probabilidad_error = random.random()
        if probabilidad_error < 0.15:
            producto["pro_nombre"] = random.choice([None, "", "  ", 12345, "producto_desconocido"])
        elif probabilidad_error < 0.35:
            producto["pro_precio"] = random.choice([None, -100, 0, "gratis", "NaN"])
        elif probabilidad_error < 0.55:
            producto["pro_codigo"] = random.choice([None, "AN99", "  ", "12345"])
        elif probabilidad_error < 0.75:
            producto["pro_stock"] = random.choice([None, -5, "mucho", 9999])

        productos.append(producto)

    return productos
