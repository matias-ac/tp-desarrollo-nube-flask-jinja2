# Práctica de Flask con Jinja2

## Requisitos de finalización

- Apertura: jueves, 4 de junio de 2026, 00:00
- Cierre: jueves, 18 de junio de 2026, 00:00

## Ejercicio 1: Aplicación básica

Crear app.py con el siguiente código:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "Hola Mundo con Flask"

if __name__ == '__main__':
    app.run(debug=True)
```


## Ejercicio 2: Uso de templates (Jinja2)

Crear templates/base.html:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```


## Ejercicio 3: Crear formulario

templates/formulario.html:

```html
{% extends 'base.html' %}

{% block content %}
<h2>Formulario de registro</h2>
<form method="POST">
    Nombre: <input type="text" name="nombre"><br>
    Email: <input type="email" name="email"><br>
    <input type="submit" value="Enviar">
</form>
{% endblock %}
```


## Ejercicio 4: Procesamiento del formulario

Modificar app.py:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        return render_template('resultado.html', nombre=nombre, email=email)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
```


Vista de resultado
templates/resultado.html:

```html
{% extends 'base.html' %}

{% block content %}
<h2>Datos recibidos</h2>
<p>Nombre: {{ nombre }}</p>
<p>Email: {{ email }}</p>
{% endblock %}
```


## Actividad práctica final

### Actividad 1: Validación de datos

- Validar que el nombre no esté vacío
- Validar formato de email
- Mostrar mensajes de error en el template usando Jinja2

### Actividad 2: Mejora del formulario

- Agregar los campos Edad (numérico) y Comentarios (textarea)
- Incorporar un campo de selección (select) con opciones (por ejemplo: carrera)

### Actividad 3: Desafío integrador

- Crear una pequeña aplicación tipo "registro de usuarios"
- Permitir alta de usuarios mediante formulario
- Mostrar listado de usuarios cargados
