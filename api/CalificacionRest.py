from flasksetup import db, mellow, Resource, request, jsonify, api, app
from flask import fields
from MatriculaRest import MatriculaSchema
from CursoMateriaRest import CursoMateriaSchema

class Calificacion (db.Model):
    id = db.Column('ID_CALIFICACION', db.Integer, primary_key = True)
    idMatricula = db.Column('ID_MATRICULA', db.Integer, db.ForeignKey('matricula.ID_MATRICULA'))
    idCursoMateria = db.Column('ID_CURSO_MATERIA', db.Integer, db.ForeignKey('curso_materia.ID_CURSO_MATERIA'))
    nota = db.Column('NOTA', db.Numeric(10,0))
    descripcion = db.Column('DESCRIPCION', db.String(1000))

    matricula = db.relationship('Matricula', backref=db.backref('_matricula', uselist=False))
    cursoMateria = db.relationship('CursoMateria', backref=db.backref('_curso_materia', uselist=False))

    def __init__(self, idMatricula, idCursoMateria, nota, descripcion):
        self.idMatricula = idMatricula
        self.idCursoMateria = idCursoMateria
        self.nota = nota
        self.descripcion = descripcion

class CalificacionSchema(mellow.Schema):
    matricula = fields.Nested(MatriculaSchema)
    cursoMateria = fields.Nested(CursoMateriaSchema)
    class Meta:
        fields = ('id', 'idMatricula', 'idCursoMateria', 'nota', 'descripcion', 'matricula', 'cursoMateria')

calificacion = CalificacionSchema()
calificacions = CalificacionSchema(many = True)

class CalificacionManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Calificacion.query.all()
            return jsonify(calificacions.dump(resultado))
        resultado = Calificacion.query.get(id)
        return jsonify(calificacion.dump(resultado))

    @staticmethod
    def post():
        idMatricula = request.json['idMatricula']
        idCursoMateria = request.json['idCursoMateria']
        nota = request.json['nota']
        descripcion = request.json['descripcion']

        nuevo = Calificacion(idMatricula, idCursoMateria, nota, descripcion)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id, 
            'resultado': f'Calificacion {descripcion} {nota} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Calificacion.query.get(id)
        current.idMatricula = request.json['idMatricula']
        current.idCursoMateria = request.json['idCursoMateria']
        current.nota = request.json['nota']
        current.descripcion = request.json['descripcion']

        db.session.commit()
        return jsonify({
            'Message': f'Calificacion {current.descripcion} {current.nota} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Calificacion.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Calificacion {current.descripcion} {current.nota} fue eliminado. '
        })

