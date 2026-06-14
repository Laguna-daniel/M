from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# AQUÍ AGREGAS TUS COSAS ROMÁNTICAS (Python las enviará a JavaScript)
DATOS_ROMANTICOS = {
    "fecha_inicio": "2024-05-15", # Cambia esta fecha por la de ustedes (Año-Mes-Día)
    "frase_principal": "Eres mi universo entero, mi principio y mi fin. ✨",
    "cartas": [
        {"id": 1, "titulo": "Nuestra primera cita", "contenido": "Ese día el universo se alineó para que te conociera. Nunca olvidaré tu sonrisa."},
        {"id": 2, "titulo": "Lo que amo de ti", "contenido": "Amo cómo iluminas mis días oscuros, exactamente como una estrella en la noche."},
        {"id": 3, "titulo": "Un deseo juntos", "contenido": "Quiero viajar por el espacio y el tiempo, pero siempre tomándote de la mano."}
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/romance')
def api_romance():
    # Calculamos los días juntos usando Python
    fecha_cita = datetime.strptime(DATOS_ROMANTICOS["fecha_inicio"], "%Y-%m-%d")
    dias_juntos = (datetime.now() - fecha_cita).days
    
    data = DATOS_ROMANTICOS.copy()
    data["dias_juntos"] = dias_juntos
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)