from datetime import datetime

def guardar_pedido(nombre, apellidos):
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        file.write(nombre + " " + apellidos + " ---- " + date + "\n")
        file.close()
