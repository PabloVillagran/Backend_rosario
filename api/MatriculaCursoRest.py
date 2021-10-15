from flasksetup import db, mellow, Resource, request, jsonify, api, app
from marshmallow import fields
from CursoRest import CursoSchema
from MatriculaRest import MatriculaSchema

class MatriculaCurso (db.Model):

    id = db.Column('ID_MATRICULA_CURSO', db.Integer, primary_key = True)
    idMatricula = db.Column('ID_MATRICULA', db.Integer, db.ForeignKey('matricula.ID_MATRICULA'))
    idCurso = db.Column('ID_CURSO', db.Integer, db.ForeignKey('curso.ID_CURSO'))
    notas = db.Column('NOTAS', db.String(1000))

    curso = db.relationship('Curso', backref=db.backref('_curso_mat', uselist=False))
    matricula = db.relationship('Matricula', backref=db.backref('_matricula_curso', uselist=False))
    
    def __init__(self, idMatricula, idCurso, notas):
        self.idMatricula = idMatricula
        self.idCurso = idCurso
        self.notas = notas

class MatriculaCursoSchema(mellow.Schema):
    curso = fields.Nested(CursoSchema)
    matricula = fields.Nested(MatriculaSchema)
    class Meta:
        fields = ('id','idMatricula', 'idCurso', 'notas', 'curso', 'matricula')

matriculaCurso = MatriculaCursoSchema()
matriculaCursos = MatriculaCursoSchema(many = True)

class MatriculaCursoManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = MatriculaCurso.query.all()
            return jsonify(matriculaCursos.dump(resultado))
        resultado = MatriculaCurso.query.get(id)
        return jsonify(matriculaCurso.dump(resultado))

    @staticmethod
    def post():
        idMatricula = request.json['idMatricula']
        idCurso = request.json['idCurso']
        notas = request.json['notas']
        descripcion = request.json['descripcion']

        nuevo = MatriculaCurso(idMatricula, idCurso, notas)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'MatriculaCurso {nuevo.idMatricula}-{nuevo.idCurso} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = MatriculaCurso.query.get(id)

        current.idMatricula = request.json['idMatricula']
        current.idCurso = request.json['idCurso']
        current.notas = request.json['notas']
        
        db.session.commit()
        return jsonify({
            'Message': f'MatriculaCurso {current.idMatricula}-{current.idCurso} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = MatriculaCurso.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'MatriculaCurso {current.descripcion} fue eliminado. '
        })
