from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
import conexion as c_params

app = Flask(__name__)
api = Api(app)
con_string = "mariadb+mysqlconnector://"+c_params.con_string
app.config['SQLALCHEMY_DATABASE_URI'] = con_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
mellow = Marshmallow(app)

class Usuario (db.Model):
  id = db.Column('ID_USUARIO', db.Integer, primary_key = True)
  usuario = db.Column('USUARIO', db.String(100))
  nombres = db.Column('NOMBRES', db.String(500))
  apellidos = db.Column('APELLIDOS', db.String(500))
  telefono = db.Column('TELEFONO', db.String(100))
  email = db.Column('EMAIL', db.String(300))  
  tipo = db.Column('ID_TIPO_USUARIO', db.Integer)
  domicilio = db.Column('DOMICILIO', db.String(1000))
  password = db.Column('PASSWORD', db.String(300))

  def __init__(self, usuario, nombres, apellidos, telefono, email, tipo, domicilio, password):
      self.usuario = usuario
      self.nombres = nombres
      self.apellidos = apellidos
      self.telefono = telefono
      self.email = email
      self.tipo = tipo
      self.domicilio = domicilio
      self.password = password

class UsuarioSchema(mellow.Schema):
    class Meta:
        fields =('usuario', 
      'nombres', 
      'apellidos', 
      'telefono', 
      'email', 
      'tipo', 
      'domicilio',
      'password')

usuario = UsuarioSchema()
usuarios = UsuarioSchema(many = True)

class UsuarioManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            rusuarios = Usuario.query.all()
            return jsonify(usuarios.dump(rusuarios))
        rusuario = Usuario.query.get(id)
        return jsonify(usuario.dump(rusuario))

    @staticmethod
    def post():
        usuario = request.json['usuario']
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        telefono = request.json['telefono']
        email = request.json['email']
        tipo = request.json['tipo']
        domicilio = request.json['domicilio']
        password = request.json['password']

        nUsuario = Usuario(usuario, nombres, apellidos, telefono, email, tipo, domicilio, password)
        db.session.add(nUsuario)
        db.session.commit()

        return jsonify({
            'resultado': f'Usuario {usuario} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })

        print('put')

    @staticmethod
    def delete():
        print('delete')

api.add_resource(UsuarioManager, '/api/usuario')
if __name__ == '__main__':
    app.run(debug=True)