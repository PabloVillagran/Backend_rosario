from flasksetup import db, mellow, Resource, request, jsonify, api, app

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
        current_user = Usuario.query.get(id)

        current_user.usuario = request.json['usuario']
        current_user.nombres = request.json['nombres']
        current_user.apellidos = request.json['apellidos']
        current_user.telefono = request.json['telefono']
        current_user.email = request.json['email']
        current_user.tipo = request.json['tipo']
        current_user.domicilio = request.json['domicilio']
        current_user.password = request.json['password']

        db.session.commit()
        return jsonify({
            'Message': f'Usuario {current_user.usuario} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current_user = Usuario.query.get(id)
        db.session.delete(current_user)
        db.session.commit()
        return jsonify({
            'Message': f'Usuario {current_user.usuario} fue eliminado. '
        })
