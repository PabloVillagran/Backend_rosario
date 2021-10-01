from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Seccion (db.Model):
    id = db.Column('ID_SECCION', db.Integer, primary_key = True)
    seccion = db.Column('SECCION', db.String(100))
  
    def __init__(self, seccion, descripcion, idSeccion, idCarrera, idGrado, ao):
        self.seccion = seccion

class SeccionSchema(mellow.Schema):
    class Meta:
        field = 'seccion'

seccion = SeccionSchema()
seccions = SeccionSchema(many = True)

class SeccionManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Seccion.query.all()
            return jsonify(seccions.dump(resultado))
        resultado = Seccion.query.get(id)
        return jsonify(seccion.dump(resultado))

    @staticmethod
    def post():
        seccion = request.json['seccion']

        nuevo = Seccion(seccion)
        db.session.add(nuevo)
        db.session.commit()

        return jsonify({
            'resultado': f'Seccion {seccion} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Seccion.query.get(id)

        current.seccion = request.json['seccion']

        db.session.commit()
        return jsonify({
            'Message': f'Seccion {current.seccion} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Seccion.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Seccion {current.seccion} fue eliminado. '
        })
