from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Alumno (db.Model):
    id = db.Column('ID_ALUMNO', db.Integer, primary_key = True)
    idUsuario = db.Column('ID_USUARIO', db.String(100))
    
    def __init__(self, idUsuario):
        self.idUsuario = idUsuario

class AlumnoSchema(mellow.Schema):
    class Meta:
        field = 'idUsuario'

alumno = AlumnoSchema()
alumnos = AlumnoSchema(many = True)

class AlumnoManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Alumno.query.all()
            return jsonify(alumnos.dump(resultado))
        resultado = Alumno.query.get(id)
        return jsonify(alumno.dump(resultado))

    @staticmethod
    def post():
        alumno = request.json['alumno']

        nuevo = Alumno(alumno)
        db.session.add(nuevo)
        db.session.commit()

        return jsonify({
            'resultado': f'Alumno {alumno} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Alumno.query.get(id)

        current.alumno = request.json['alumno']

        db.session.commit()
        return jsonify({
            'Message': f'Alumno {current.alumno} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Alumno.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Alumno {current.alumno} fue eliminado. '
        })

