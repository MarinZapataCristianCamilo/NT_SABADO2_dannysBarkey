import random
from datetime import datetime, timedelta


def simular_ventas(numeroVentas):
    ventas = []
    fecha_inicio = datetime.now() - timedelta(days=365)
    codigos_usuarios = ["AN01", "AN02", "AN03", "AN04", "AN05"]

    for i in range(1, numeroVentas + 1):
        fecha = fecha_inicio + timedelta(days=random.randint(0, 365))
        ventas.append(
            {
                "ven_codigo": f"V{10000 + i}",
                "ven_fecha": fecha.date().isoformat(),
                "ven_total": round(random.uniform(500.0, 5000.0), 2),
                "usu_codigo": random.choice(codigos_usuarios),
                "emp_codigo": random.randint(1001, 1010),
            }
        )

    return ventas
