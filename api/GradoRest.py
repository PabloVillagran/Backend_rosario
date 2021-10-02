from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Grado (db.Model):
    id = db.Column('ID_GRADO', db.Integer, primary_key = True)
    grado = db.Column('GRADO', db.String(100))
  
    def __init__(self, grado):
        self.grado = grado

class GradoSchema(mellow.Schema):
    class Meta:
        fields = ('id','grado')

grado = GradoSchema()
grados = GradoSchema(many = True)

class GradoManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Grado.query.all()
            return jsonify(grados.dump(resultado))
        resultado = Grado.query.get(id)
        return jsonify(grado.dump(resultado))

    @staticmethod
    def post():
        grado = request.json['grado']

        nuevo = Grado(grado)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'Grado {grado} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Grado.query.get(id)

        current.grado = request.json['grado']

        db.session.commit()
        return jsonify({
            'Message': f'Grado {current.grado} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Grado.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Grado {current.grado} fue eliminado. '
        })

