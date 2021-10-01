
class Usuario (db.Model):
  id = db.Column('ID_USUARIO', db.Integer, primary_key = True)
  usuario = db.Column('USUARIO', db.String(100))
  nombres = db.Column('NOMBRES', db.String(500))
  apellidos = db.Column('APELLIDOS', db.String(500))
  telefono = db.Column('TELEFONO', db.String(100))
  email = db.Column('EMAIL', db.String(300))  
  tipo = db.Column('ID_TIPO_USUARIO', db.Integer)
  domicilio = db.Column('DOMICILIO', db.String(1000))

  def __init__(self, usuario, nombres, apellidos, telefono, email, tipo, domicilio):
      self.usuario = usuario
      self.nombres = nombres
      self.apellidos = apellidos
      self.telefono = telefono
      self.email = email
      self.tipo = tipo
      self.domicilio = domicilio