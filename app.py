import os

from flask import Flask, flash, render_template, request

from validaciones_form import es_edad_correcta, es_email_correcto, es_nombre_correcto

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

CARRERAS = {
    "analisis": "Análisis de Sistemas",
    "desarrollo": "Desarrollo de Software",
    "datos": "Ciencia de Datos",
}


def renderizar_formulario_con_valores(nombre, email, edad, carrera, comentarios):
    return render_template(
        "formulario.html",
        nombre=nombre,
        email=email,
        edad=edad,
        carrera=carrera,
        comentarios=comentarios,
    )


@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        edad = request.form["edad"]
        comentarios = request.form["comentarios"]
        carrera = request.form["carrera"]

        if not es_nombre_correcto(nombre):
            flash(
                "Debe ingresar un nombre con caracteres válidos (alfabéticos)",
                "nombre_error",
            )
            return renderizar_formulario_con_valores(
                nombre, email, edad, carrera, comentarios
            )

        if not es_email_correcto(email):
            flash(
                "Debe ingresar un email con formato válido (ej.: email@email.com)",
                "email_error",
            )
            return renderizar_formulario_con_valores(
                nombre, email, edad, carrera, comentarios
            )

        if not es_edad_correcta(edad):
            flash("Debe ingresar su edad correctamente (número entero)", "edad_error")
            return renderizar_formulario_con_valores(
                nombre, email, edad, carrera, comentarios
            )

        if len(str(comentarios)) > 500:
            flash("Máximo 500 caracteres", "comentarios_error")
            return renderizar_formulario_con_valores(
                nombre, email, edad, carrera, comentarios
            )

        if carrera == "":
            flash("Por favor, seleccioná una carrera de la lista", "carrera_error")
            return renderizar_formulario_con_valores(
                nombre, email, edad, carrera, comentarios
            )

        return render_template(
            "resultado.html",
            nombre=nombre,
            email=email,
            edad=edad,
            carrera=CARRERAS[carrera],
            comentarios=comentarios,
        )
    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)
