from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la conexión a la base de datos MySQL remota
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://hugo_moreno:Hvallekano1311@db4free.net:3306/iesdawhugom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hardsecretkey'

db = SQLAlchemy(app)

# Modelo de la tabla de alimentos (o la tabla que desees leer)
class Alimento(db.Model):
    __tablename__ = 'alimentos'  # Reemplaza 'nombre_tabla' con el nombre de tu tabla en db4free
    # Define las columnas de tu tabla (deben coincidir con la estructura de tu tabla)
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    marca = db.Column(db.String(100), nullable=False)

# Ruta para mostrar los alimentos desde la base de datos MySQL remota
@app.route('/')
def mostrar_alimentos():
    alimentos = Alimento.query.all()
    return render_template('index.html', alimentos=alimentos)

@app.route('/insertar_ejemplos')
def insertar_ejemplos():
    manzana = Alimento(id=1, nombre='Manzana', precio=1.5, marca='Marca A')
    banana = Alimento(id=2, nombre='Banana', precio=2.0, marca='Marca B')
    yogurt = Alimento(id=3, nombre='Yogurt', precio=1.0, marca='Marca C')
    
    db.session.add(manzana)
    db.session.add(banana)
    db.session.add(yogurt)
    
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)

