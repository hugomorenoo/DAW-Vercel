from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Ruta para mostrar los alimentos desde la base de datos
@app.route('/')
def mostrar_alimentos():
    conn = sqlite3.connect('alimentos.sql')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alimentos')
    alimentos = cursor.fetchall()
    conn.close()
    return render_template('index.html', alimentos=alimentos)

if __name__ == '__main__':
    app.run(debug=True)