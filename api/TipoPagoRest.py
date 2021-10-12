from flasksetup import db, mellow, Resource, request, jsonify, api, app

class TipoPago (db.Model):
    id = db.Column('ID_TIPO_PAGO', db.Integer, primary_key = True)
    tipoPago = db.Column('TIPO_PAGO', db.String(300))
    descripcion = db.Column('DESCRIPCION', db.String(1000))
    
    def __init__(self, tipoPago, descripcion):
        self.tipoPago = tipoPago
        self.descripcion = descripcion

class TipoPagoSchema(mellow.Schema):
    class Meta:
        fields = ('id','tipoPago', 'descripcion')

tipoPago = TipoPagoSchema()
tipoPagos = TipoPagoSchema(many = True)

class TipoPagoManager(Resource):
    pass

    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            resultado = TipoPago.query.all()
            return jsonify(tipoPagos.dump(resultado))
        resultado = TipoPago.query.get(id)
        return jsonify(tipoPago.dump(resultado))

    @staticmethod
    def post():
        tipoPago = request.json['tipoPago']
        descripcion = request.json['descripcion']

        nuevo = TipoPago(tipoPago, descripcion)
        db.session.add(nuevo)
        db.session.flush()
        db.session.refresh(nuevo)
        db.session.commit()

        return jsonify({
            'id':nuevo.id,
            'resultado': f'TipoPago {descripcion} creado.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = TipoPago.query.get(id)

        current.tipoPago = request.json['tipoPago']
        current.descripcion = request.json['descripcion']

        db.session.commit()
        return jsonify({
            'Message': f'TipoPago {current.descripcion} fue actualizado. '
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({
                'resultado': f'Id {id} no encontrado.'
            })
        current = TipoPago.query.get(id)
        db.session.delete(current)
        db.session.commit()
        return jsonify({
            'Message': f'TipoPago {current.descripcion} fue eliminado. '
        })


