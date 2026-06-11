import re

from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
app.secret_key = "super_secret"

email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        print(request)
        print(f"nombre: {nombre}")
        print(f"email: {email}")

        if len(nombre) < 1:
            flash("El campo 'nombre' no puede estar vacío", "nombre_error")
            return render_template("formulario.html", nombre=nombre, email=email)

        if not re.fullmatch(email_pattern, email):
            flash("Email con formato inválido", "email_error")
            return render_template("formulario.html", nombre=nombre, email=email)

        return render_template("resultado.html", nombre=nombre, email=email)
    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)
