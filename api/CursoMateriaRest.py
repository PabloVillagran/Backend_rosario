from flasksetup import db, mellow, Resource, request, jsonify, api, app
from marshmallow import fields
from HorarioRest import Horario, HorarioSchema
from MateriaRest import Materia, MateriaSchema
from CursoRest import Curso, CursoSchema
from ProfesorRest import ProfesorSchema

class CursoMateria (db.Model):
    id = db.Column('ID_CURSO_MATERIA', db.Integer, primary_key = True)
    idCurso = db.Column('ID_CURSO', db.Integer, db.ForeignKey('curso.ID_CURSO'))
    idMateria = db.Column('ID_MATERIA', db.Integer, db.ForeignKey('materia.ID_MATERIA'))
    idHorario = db.Column('ID_HORARIO', db.Integer, db.ForeignKey('horario.ID_HORARIO'))
    idProfesor = db.Column('ID_PROFESOR', db.Integer, db.ForeignKey('profesor.ID_PROFESOR'))
    descripcion = db.Column('DESCRIPCION', db.String(1000))

    curso = db.relationship('Curso', backref=db.backref('_curso', uselist=False))
    materia = db.relationship('Materia', backref=db.backref('_materia', uselist=False))
    horario = db.relationship('Horario', backref=db.backref('_horario', uselist=False))
    profesor = db.relationship('Profesor', backref=db.backref('_profesor', uselist=False))
    
    def __init__(self, idHorario, idMateria, idCurso, descripcion, idProfesor):
        self.idHorario = idHorario
        self.idMateria = idMateria
        self.idCurso = idCurso
        self.descripcion = descripcion
        self.idProfesor = idProfesor

class CursoMateriaSchema(mellow.Schema):
    curso = fields.Nested(CursoSchema)
    materia = fields.Nested(MateriaSchema)
    horario = fields.Nested(HorarioSchema)
    profesor = fields.Nested(ProfesorSchema)
    class Meta:
        fields = ('id','idHorario', 'idMateria', 'idCurso', 'descripcion', 'idProfesor', 'curso', 'materia', 'horario', 'profesor')

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
            'Message': f'CursoMateria {current.descripcion} fue actualizado. '
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
            'Message': f'CursoMateria {current.descripcion} fue eliminado. '
        })

