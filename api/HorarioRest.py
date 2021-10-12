from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Horario (db.Model):

    id = db.Column('ID_HORARIO', db.Integer, primary_key = True)
    horaInicio = db.Column('HORA_INICIO', db.Time)
    horaFin = db.Column('HORA_FIN', db.time)
    descripcion = db.Column('DESCRIPCION', db.String(500))
    
    def __init__(self, horaInicio, horaFin, descripcion):
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.descripcion = descripcion

class HorarioSchema(mellow.Schema):
    class Meta:
        fields = ('id','horaInicio', 'horaFin', 'descripcion')

horario = HorarioSchema()
horarios = HorarioSchema(many = True)

class HorarioManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Horario.query.all()
            return jsonify(horarios.dump(resultado))
        resultado = Horario.query.get(id)
        return jsonify(horario.dump(resultado))

    @staticmethod
    def post():
        horaInicio = request.json['horaInicio']
        horaFin = request.json['horaFin']
        descripcion = request.json['descripcion']

        nuevo = Horario(horario, horaInicio, horaFin, descripcion)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'Horario {horario} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Horario.query.get(id)

        current.horaInicio = request.json['horaInicio']
        current.horaFin = request.json['horaFin']
        current.descripcion = request.json['descripcion']
        
        db.session.commit()
        return jsonify({
            'Message': f'Horario {current.descripcion} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Horario.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Horario {current.descripcion} fue eliminado. '
        })
