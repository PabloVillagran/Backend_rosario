#  ID_CURSO_MATERIA int NOT NULL AUTO_INCREMENT PRIMARY KEY,
#  ID_HORARIO int NOT NULL,
#  ID_MATERIA int NOT NULL,
#  ID_CURSO int NOT NULL,
#  DESCRIPCION varchar(1000) NOT NULL,
#  ID_PROFESOR int NOT NULL

from flasksetup import db, mellow, Resource, request, jsonify, api, app

class CursoMateria (db.Model):
    id = db.Column('ID_CURSO_MATERIA', db.Integer, primary_key = True)
    idHorario = db.Column('ID_HORARIO', db.Integer)
    idMateria = db.Column('ID_MATERIA', db.Integer)
    idCurso = db.Column('ID_CURSO', db.Integer)
    descripcion = db.Column('DESCRIPCION', db.String(1000))
    idProfesor = db.Column('ID_PROFESOR', db.Integer)
    
    def __init__(self, idHorario, idMateria, idCurso, descripcion, idProfesor):
        self.idHorario = idHorario
        self.idMateria = idMateria
        self.idCurso = idCurso
        self.descripcion = descripcion
        self.idProfesor = idProfesor

class CursoMateriaSchema(mellow.Schema):
    class Meta:
        fields = ('id','idHorario', 'idMateria', 'idCurso', 'descripcion', 'idProfesor')

cursoMateria = CursoMateriaSchema()
cursoMaterias = CursoMateriaSchema(many = True)

class CursoMateriaManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = CursoMateria.query.all()
            return jsonify(cursoMaterias.dump(resultado))
        resultado = CursoMateria.query.get(id)
        return jsonify(cursoMateria.dump(resultado))

    @staticmethod
    def post():
        idHorario = request.json['idHorario']
        idMateria = request.json['idMateria']
        idCurso = request.json['idCurso']
        descripcion = request.json['descripcion']
        idProfesor = request.json['idProfesor']

        nuevo = CursoMateria(idHorario, idMateria, idCurso, descripcion, idProfesor)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'CursoMateria {descripcion} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = CursoMateria.query.get(id)
        current.idHorario = request.json['idHorario']
        current.idMateria = request.json['idMateria']
        current.idCurso = request.json['idCurso']
        current.descripcion = request.json['descripcion']
        current.idProfesor = request.json['idProfesor']

        db.session.commit()
        return jsonify({
            'Message': f'CursoMateria {current.descripcion} {current.nota} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = CursoMateria.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'CursoMateria {current.descripcion} {current.nota} fue eliminado. '
        })

