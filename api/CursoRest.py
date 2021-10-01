from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Curso (db.Model):
    id = db.Column('ID_CURSO', db.Integer, primary_key = True)
    curso = db.Column('CURSO', db.String(100))
    descripcion = db.Column('DESCRIPCION', db.String(1000))
    idSeccion = db.Column('ID_SECCION', db.Integer)
    idCarrera = db.Column('ID_CARRERA', db.Integer)
    idGrado = db.Column('ID_GRADO', db.Integer)
    ao = db.Column('AO', db.Integer)
  
    def __init__(self, curso, descripcion, idSeccion, idCarrera, idGrado, ao):
        self.curso = curso
        self.descripcion = descripcion
        self.idSeccion = idSeccion
        self.idCarrera = idCarrera
        self.idGrado = idGrado
        self.ao = ao

class CursoSchema(mellow.Schema):
    class Meta:
        fields =('curso', 'descripcion', 'idSeccion', 'idCarrera', 'idGrado', 'ao')

curso = CursoSchema()
cursos = CursoSchema(many = True)

class CursoManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Curso.query.all()
            return jsonify(cursos.dump(resultado))
        resultado = Curso.query.get(id)
        return jsonify(curso.dump(resultado))

    @staticmethod
    def post():
        curso = request.json['curso']
        descripcion = request.json['descripcion']
        idSeccion = request.json['idSeccion']
        idCarrera = request.json['idCarrera']
        idGrado = request.json['idGrado']
        ao = request.json['ao']

        nuevo = Curso(curso, descripcion, idSeccion, idCarrera, idGrado, ao)
        db.session.add(nuevo)
        db.session.commit()

        return jsonify({
            'resultado': f'Curso {curso} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Curso.query.get(id)

        current.curso = request.json['curso']
        current.descripcion = request.json['descripcion']
        current.idSeccion = request.json['idSeccion']
        current.idCarrera = request.json['idCarrera']
        current.idGrado = request.json['idGrado']
        current.ao = request.json['ao']

        db.session.commit()
        return jsonify({
            'Message': f'Curso {current.curso} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current_user = Curso.query.get(id)
        db.session.delete(current_user)
        db.session.commit()
        return jsonify({
            'Message': f'Curso {current_user.curso} fue eliminado. '
        })

