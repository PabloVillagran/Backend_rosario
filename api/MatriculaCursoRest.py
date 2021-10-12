from flasksetup import db, mellow, Resource, request, jsonify, api, app

class MatriculaCurso (db.Model):

    id = db.Column('ID_MATRICULA_CURSO', db.Integer, primary_key = True)
    idMatricula = db.Column('ID_MATRICULA', db.Integer)
    idCurso = db.Column('ID_CURSO', db.Integer)
    notas = db.Column('NOTAS', db.String(1000))
    
    def __init__(self, idMatricula, idCurso, notas):
        self.idMatricula = idMatricula
        self.idCurso = idCurso
        self.notas = notas

class MatriculaCursoSchema(mellow.Schema):
    class Meta:
        fields = ('id','idMatricula', 'idCurso', 'notas')

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
