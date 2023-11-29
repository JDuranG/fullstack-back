"""
Backend Fullstack Pizza
"""

from flask import Flask, request, redirect, Response
from persistencia import guardar_pedido
app = Flask(__name__)

@app.route("/pizza",methods=['POST'])
def pedido_pizza():
    """
    Pedido Pizza
    """
    print("Pedido Pizza POST")
    nombre= request.form.get("fname")
    apellidos = request.form.get("lname")
    print(nombre)
    print(apellidos)
    guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    tamaño = request.form.get("size")
    print(tamaño)
    mensaje = "Disponible"
    if tamaño == "S":
        mensaje = "No disponible"
    print(mensaje)
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})