from flasksetup import db, mellow, Resource, request, jsonify, api, app
from marshmallow import fields
from AlumnoRest import AlumnoSchema

class Matricula (db.Model):

    id = db.Column('ID_MATRICULA', db.Integer, primary_key = True)
    fechaIngreso = db.Column('FECHA_INGRESO', db.DateTime)
    fechaEgreso = db.Column('FECHA_EGRESO', db.DateTime)
    ao = db.Column('AO', db.Integer)
    idAlumno = db.Column('ID_ALUMNO', db.Integer, db.ForeignKey('alumno.ID_ALUMNO'))
    nota = db.Column('NOTAS', db.String(1000))

    alumno = db.relationship('Alumno', backref=db.backref('_alumno', uselist=False))

    def __init__(self, fechaIngreso, fechaEgreso, ao, idAlumno, nota):
        self.fechaIngreso = fechaIngreso
        self.fechaEgreso = fechaEgreso
        self.ao = ao
        self.idAlumno = idAlumno
        self.nota = nota

class MatriculaSchema(mellow.Schema):
    alumno = fields.Nested(AlumnoSchema)
    class Meta:
        fields = ('id','fechaIngreso', 'fechaEgreso', 'ao', 'idAlumno', 'nota', 'alumno')

matricula = MatriculaSchema()
matriculas = MatriculaSchema(many = True)

class MatriculaManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Matricula.query.all()
            return jsonify(matriculas.dump(resultado))
        resultado = Matricula.query.get(id)
        return jsonify(matricula.dump(resultado))

    @staticmethod
    def post():
        fechaIngreso = request.json['fechaIngreso']
        fechaEgreso = request.json['fechaEgreso']
        ao = request.json['ao']
        idAlumno = request.json['idAlumno']
        nota = request.json['nota']

        nuevo = Matricula(fechaIngreso, fechaEgreso, ao, idAlumno, nota)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'Matricula para el alumno {idAlumno} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Matricula.query.get(id)

        current.fechaIngreso = request.json['fechaIngreso']
        current.fechaEgreso = request.json['fechaEgreso']
        current.ao = request.json['ao']
        current.idAlumno = request.json['idAlumno']
        current.nota = request.json['nota']
        
        db.session.commit()
        return jsonify({
            'Message': f'Matricula {current.id} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Matricula.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Matricula {current.id} fue eliminado. '
        })
