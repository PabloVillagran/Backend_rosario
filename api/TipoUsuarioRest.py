from flasksetup import db, mellow, Resource, request, jsonify, api, app

class TipoUsuario (db.Model):
    id = db.Column('ID_TIPO_USUARIO', db.Integer, primary_key = True)
    tipoUsuario = db.Column('TIPO_USUARIO', db.String(100))
    descripcion = db.Column('DESCRIPCION', db.String(1000))
    
    def __init__(self, tipoUsuario, descripcion):
        self.tipoUsuario = tipoUsuario
        self.descripcion = descripcion

class TipoUsuarioSchema(mellow.Schema):
    class Meta:
        fields = ('id','tipoUsuario', 'descripcion')

tipoUsuario = TipoUsuarioSchema()
tipoUsuarios = TipoUsuarioSchema(many = True)

class TipoUsuarioManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = TipoUsuario.query.all()
            return jsonify(tipoUsuarios.dump(resultado))
        resultado = TipoUsuario.query.get(id)
        return jsonify(tipoUsuario.dump(resultado))

    @staticmethod
    def post():
        tipoUsuario = request.json['tipoUsuario']
        descripcion = request.json['descripcion']

        nuevo = TipoUsuario(tipoUsuario, descripcion)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'TipoUsuario {descripcion} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = TipoUsuario.query.get(id)

        current.tipoUsuario = request.json['tipoUsuario']
        current.descripcion = request.json['descripcion']

        db.session.commit()
        return jsonify({
            'Message': f'TipoUsuario {current.descripcion} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = TipoUsuario.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'TipoUsuario {current.tipoUsuario} fue eliminado. '
        })


