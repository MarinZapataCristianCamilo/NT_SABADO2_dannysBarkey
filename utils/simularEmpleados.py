import random


def simular_empleados(numeroEmpleados):
    nombres = ["robert", "adelaida", "mariana", "isabela"]
    cargos = ["panadero", "pastelero", "vendedor", "administrador"]
    salarios = [1800.00, 2200.50, 1500.75, 3000.00, 4200.25]

    empleados = []

    for _ in range(numeroEmpleados):
        nombre = random.choice(nombres)
        empleado = {
            "emp_codigo": random.randint(1000, 9999),
            "emp_nombre": nombre,
            "emp_email": f"{nombre}@example.com",
            "emp_id": str(random.randint(100000, 999999)),
            "emp_cargo": random.choice(cargos),
            "emp_salario": round(random.choice(salarios), 2)
        }

        probabilidad_error = random.random()
        if probabilidad_error < 0.15:
            empleado["emp_nombre"] = random.choice([None, "NaN", "", "  ", "juan"])
        elif probabilidad_error < 0.30:
            empleado["emp_email"] = random.choice([None, "invalid_email", "missing@", "@example.com", "EMPLOYE1@EXAMPLE.COM"])
        elif probabilidad_error < 0.45:
            empleado["emp_cargo"] = random.choice([None, "", "  ", "cajero123"])
        elif probabilidad_error < 0.55:
            empleado["emp_codigo"] = random.choice([None, -1, 0, 99999, "ABCD"])
        elif probabilidad_error < 0.70:
            empleado["emp_salario"] = random.choice([None, -100.00, 0, "NaN", "gratis"])
        elif probabilidad_error < 0.85:
            empleado["emp_id"] = random.choice([None, "", "abc123", "12345678901", -1])

        empleados.append(empleado)

    return empleados
