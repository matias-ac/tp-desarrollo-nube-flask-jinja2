from flask import Flask, flash, render_template, request

from utils import es_email_correcto

app = Flask(__name__)
app.secret_key = "super_secret"


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

        if not es_email_correcto(email):
            flash("Email con formato inválido", "email_error")
            return render_template("formulario.html", nombre=nombre, email=email)

        return render_template("resultado.html", nombre=nombre, email=email)
    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)
