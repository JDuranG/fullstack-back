"""
Persistencia
"""

def guardar_pedido(nombre, apellidos):
    """
    Guardar pedido en un txt
    """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
