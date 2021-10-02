from flasksetup import db, mellow, Resource, request, jsonify, api, app
from UsuarioRest import Usuario

class Administrativo (db.Model):
    id = db.Column('ID_ADMINISTRATIVO', db.Integer, primary_key = True)
    idUsuario = db.Column('ID_USUARIO', db.String(100))
    
    def __init__(self, idUsuario):
        self.idUsuario = idUsuario

class AdministrativoSchema(mellow.Schema):
    class Meta:
        fields = ('id', 'idUsuario')

administrativo = AdministrativoSchema()
administrativos = AdministrativoSchema(many = True)

class AdministrativoManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Administrativo.query.all()
            return jsonify(administrativos.dump(resultado))
        resultado = Administrativo.query.get(id)
        return jsonify(administrativo.dump(resultado))

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
        nuevo = Administrativo(idUsuario)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()
        
        return jsonify({
            'id':nuevo.id,
            'resultado': f'Administrativo {idUsuario} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Administrativo.query.get(id)

        current.administrativo = request.json['administrativo']

        db.session.commit()
        return jsonify({
            'Message': f'Administrativo {current.administrativo} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Administrativo.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Administrativo {current.administrativo} fue eliminado. '
        })

