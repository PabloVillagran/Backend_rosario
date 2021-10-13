from flasksetup import db, mellow, Resource, request, jsonify, api, app

class Pago (db.Model):

    id = db.Column('ID_PAGO', db.Integer, primary_key = True)
    monto = db.Column('MONTO', db.Numeric(10,0))
    descripcion = db.Column('DESCRIPCION', db.String(1000))
    idMatricula = db.Column('ID_MATRICULA', db.Integer)
    idTipoPago = db.Column('ID_TIPO_PAGO', db.Integer)
    fechaVencimiento = db.Column('FECHA_VENCIMIENTO', db.DateTime)
    fechaPago = db.Column('FECHA_PAGO', db.DateTime)
    
    def __init__(self, monto, descripcion, idMatricula, idTipoPago, fechaVencimiento, fechaPago):
        self.fechaIngreso = monto
        self.fechaEgreso = descripcion
        self.ao = idMatricula
        self.idAlumno = idTipoPago
        self.nota = fechaVencimiento
        self.fechaPago = fechaPago

class PagoSchema(mellow.Schema):
    class Meta:
        fields = ('id', 'monto', 'descripcion', 'idMatricula', 'idTipoPago', 'fechaVencimiento', 'fechaPago')

pago = PagoSchema()
pagos = PagoSchema(many = True)

class PagoManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = Pago.query.all()
            return jsonify(pagos.dump(resultado))
        resultado = Pago.query.get(id)
        return jsonify(pago.dump(resultado))

    @staticmethod
    def post():
        monto = request.json['monto']
        descripcion = request.json['descripcion']
        idMatricula = request.json['idMatricula']
        idTipoPago = request.json['idTipoPago']
        fechaVencimiento = request.json['fechaVencimiento']
        fechaPago = request.json['fechaPago']

        nuevo = Pago(monto, descripcion, idMatricula, idTipoPago, fechaVencimiento, fechaPago)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'Pago para el alumno {nuevo.id} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Pago.query.get(id)

        current.monto = request.json['monto']
        current.descripcion = request.json['descripcion']
        current.idMatricula = request.json['idMatricula']
        current.idTipoPago = request.json['idTipoPago']
        current.fechaVencimiento = request.json['fechaVencimiento']
        current.fechaPago = request.json['fechaPago']
        
        db.session.commit()
        return jsonify({
            'Message': f'Pago {current.id} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = Pago.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'Pago {current.id} fue eliminado. '
        })
