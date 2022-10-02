from tarea07 import app
from flask import render_template, redirect, session #redirect nos redirecciona a otra pagina -- session es un diccionario, almacena informacion de una variable y puede ser utilizada en cualquier parte del codigo o documento

@app.route("/") #su suma 1 a las visitas
def contador():
    if "contador_visitas" in session: #si la variable ya contiene informacion que sume 1
        session["contador_visitas"] += 1
    else:
        session["contador_visitas"] = 1 #si no tiene informacion que empiece en 1
    return render_template("index.html") 

@app.route("/destruir_sesion") #elimina el contenido almacenado en todas las sesiones
def eliminar_sesion():
    session.clear()
    return redirect("/")

@app.route("/sumando_visitas") #su suma 1 a las visitas
def sumar():
    session["contador_visitas"] += 1
    return redirect("/")

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return  'ESTA RUTA NO FUE ENCONTRADA', 404