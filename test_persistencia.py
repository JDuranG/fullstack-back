from persistencia import guardar_pedido

with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

pedidos = [{"nombre":"Juancho", "apellidos":"garcia"},{"nombre":"Antonio", "apellidos":"perez sanchez"},{"nombre":"Javier", "apellidos":"Duran"},{"nombre":"Monica", "apellidos":"parker"},]
for persona in pedidos:
    nombre = persona['nombre']
    apellidos = persona['apellidos']
    guardar_pedido(nombre, apellidos)