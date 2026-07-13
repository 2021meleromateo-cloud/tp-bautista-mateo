from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

preguntas = [
    {
        "pregunta": "¿Cuántos jugadores tiene un equipo en la cancha al comenzar un partido?",
        "opciones": ["9", "10", "11", "12"],
        "correcta": "11"
    },
    {
        "pregunta": "¿Qué selección ganó el Mundial de Qatar 2022?",
        "opciones": ["Argentina", "Francia", "Brasil", "Croacia"],
        "correcta": "Argentina"
    },
    {
        "pregunta": "¿Cuántos minutos dura un partido de fútbol?",
        "opciones": ["80", "90", "100", "120"],
        "correcta": "90"
    },
    {
        "pregunta": "¿Qué jugador es conocido como 'La Pulga'?",
        "opciones": [
            "Cristiano Ronaldo",
            "Lionel Messi",
            "Neymar",
            "Mbappé"
        ],
        "correcta": "Lionel Messi"
    },
    {
        "pregunta": "¿Qué tarjeta expulsa a un jugador?",
        "opciones": [
            "Amarilla",
            "Azul",
            "Roja",
            "Verde"
        ],
        "correcta": "Roja"
    }
]


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        puntaje = 0

        for i, pregunta in enumerate(preguntas):

            respuesta = request.form.get(f"pregunta{i}")

            if respuesta == pregunta["correcta"]:
                puntaje += 1

        return render_template(
            "resultado.html",
            puntaje=puntaje,
            total=len(preguntas)
        )


    preguntas_juego = []

    for pregunta in preguntas:

        opciones = pregunta["opciones"][:]
        random.shuffle(opciones)

        preguntas_juego.append({
            "pregunta": pregunta["pregunta"],
            "opciones": opciones
        })


    return render_template(
        "index.html",
        preguntas=preguntas_juego
    )


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
