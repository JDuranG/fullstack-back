from flask import Flask, request, redirect
from persistencia import guardar_pedido
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<html><body><p>Hello, World!</p></body></html>"


@app.route("/pizza",methods=['POST'])
def pedido_pizza():
    print("Pedido Pizza POST")
    nombre= request.form.get("fname")
    apellidos = request.form.get("lname")
    print(nombre)
    print(apellidos)
    guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/solicita_pedido.html", code=302)
