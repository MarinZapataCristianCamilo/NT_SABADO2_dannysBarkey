import random
#panaderia dannysBarkey 
def simular_productos(numeroProductos):
    pro_nombres = ["pan", "pastel", "galleta", "croissant"]
    pro_precios = [1500, 2500, 500, 2000]
    pro_codigos = ["AN01", "AN02", "AN03", "AN04", "AN05"]
    pro_stock = [10, 20, 30, 40, 50]

    productos = []

    for _ in range(numeroProductos):
        producto = {
            "pro_nombre": random.randint(0, 5000 ),
            "pro_precio": random.choice(pro_precios),
            "pro_codigo": random.choice(pro_codigos),
            "pro_stock": random.choice(pro_stock)
        }
        productos.append(producto)

    return productos
