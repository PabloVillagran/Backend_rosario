#  ID_CALIFICACION int NOT NULL AUTO_INCREMENT PRIMARY KEY,
#  ID_MATRICULA int NOT NULL,
#  ID_CURSO_MATERIA int NOT NULL,
#  NOTA decimal(10,0) NOT NULL,
#  DESCRIPCION varchar(1000) NOT NULL, 

from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Calificacion (db.Model):
    id = db.Column('ID_CALIFICACION', db.Integer, primary_key = True)
    idMatricula = db.Column('ID_MATRICULA', db.Integer)
    idCursoMateria = db.Column('ID_CURSO_MATERIA', db.Integer)
    nota = db.Column('NOTA', db.Numeric(10,0))
    descripcion = db.Column('DESCRIPCION', db.String(1000))
    
    def __init__(self, idMatricula, idCursoMateria, nota, descripcion):
        self.idMatricula = idMatricula
        self.idCursoMateria = idCursoMateria
        self.nota = nota
        self.descripcion = descripcion

class CalificacionSchema(mellow.Schema):
    class Meta:
        fields = ('idMatricula', 'idCursoMateria', 'nota', 'descripcion')

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
        db.session.commit()

        return jsonify({
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

