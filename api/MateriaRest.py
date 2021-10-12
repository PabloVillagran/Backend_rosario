from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Materia (db.Model):
    id = db.Column('ID_MATERIA', db.Integer, primary_key = True)
    materia = db.Column('MATERIA', db.String(300))
    descripcion = db.Column('DESCRIPCION', db.String(1000))
    
    def __init__(self, materia, descripcion):
        self.materia = materia
        self.descripcion = descripcion

class MateriaSchema(mellow.Schema):
    class Meta:
        fields = ('id','materia', 'descripcion')

materia = MateriaSchema()
materias = MateriaSchema(many = True)

class MateriaManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Materia.query.all()
            return jsonify(materias.dump(resultado))
        resultado = Materia.query.get(id)
        return jsonify(materia.dump(resultado))

    @staticmethod
    def post():
        materia = request.json['materia']
        descripcion = request.json['descripcion']

        nuevo = Materia(materia, descripcion)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'Materia {materia} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Materia.query.get(id)

        current.materia = request.json['materia']
        current.descripcion = request.json['descripcion']

        db.session.commit()
        return jsonify({
            'Message': f'Materia {current.materia} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Materia.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Materia {current.materia} fue eliminado. '
        })


