from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Carrera (db.Model):
    id = db.Column('ID_CARRERA', db.Integer, primary_key = True)
    carrera = db.Column('CARRERA', db.String(100))
    cursos = db.relationship('Curso', backref='carrera', lazy=True)
  
    def __init__(self, carrera):
        self.carrera = carrera

class CarreraSchema(mellow.Schema):
    class Meta:
        fields = ('id','carrera')

carrera = CarreraSchema()
carreras = CarreraSchema(many = True)

class CarreraManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Carrera.query.all()
            return jsonify(carreras.dump(resultado))
        resultado = Carrera.query.get(id)
        return jsonify(carrera.dump(resultado))

    @staticmethod
    def post():
        carrera = request.json['carrera']

        nuevo = Carrera(carrera)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'Carrera {carrera} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Carrera.query.get(id)

        current.carrera = request.json['carrera']

        db.session.commit()
        return jsonify({
            'Message': f'Carrera {current.carrera} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Carrera.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Carrera {current.carrera} fue eliminado. '
        })

