from flasksetup import db, mellow, Resource, request, jsonify, api, app
from marshmallow import fields
from UsuarioRest import Usuario, UsuarioSchema

class Profesor (db.Model):
  id = db.Column('ID_PROFESOR', db.Integer, primary_key = True)
  idUsuario = db.Column('ID_USUARIO', db.Integer, db.ForeignKey('usuario.ID_USUARIO'))

  usuario = db.relationship('Usuario', backref=db.backref('_usuario', uselist=False))
  
  def __init__(self, idUsuario):
    self.idUsuario = idUsuario

class ProfesorSchema(mellow.Schema):
    usuario = fields.Nested(UsuarioSchema)
    class Meta:
        fields = ('id', 'idUsuario')

profesor = ProfesorSchema()
profesors = ProfesorSchema(many = True)

class ProfesorManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Profesor.query.all()
            return jsonify(profesors.dump(resultado))
        resultado = Profesor.query.get(id)
        return jsonify(profesor.dump(resultado))

    @staticmethod
    def post():
        try:
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
            db.session.flush()
            db.session.refresh(nUsuario)
        except Exception as _e:
            return jsonify({
                'err': f'{_e}'
            })

        idUsuario = nUsuario.id
        nuevo = Profesor(idUsuario)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()
        
        return jsonify({
            'id':nuevo.id,
            'resultado': f'Profesor {idUsuario} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Profesor.query.get(id)

        current.idUsuario = request.json['idUsuario']

        db.session.commit()
        return jsonify({
            'Message': f'Profesor {current.idUsuario} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Profesor.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Profesor {current.profesor} fue eliminado. '
        })

