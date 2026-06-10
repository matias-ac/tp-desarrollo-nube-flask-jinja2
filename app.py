from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "super_secret"


@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]

        if len(nombre) < 1:
            flash("El campo 'nombre' no puede estar vacío")
            return redirect("/")

        return render_template("resultado.html", nombre=nombre, email=email)
    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)
