import flasksetup as flask
import CursoRest
import SeccionRest
import UsuarioRest
import CarreraRest

flask.api.add_resource(CarreraRest.CarreraManager, '/api/carrera')
flask.api.add_resource(CursoRest.CursoManager, '/api/curso')
flask.api.add_resource(SeccionRest.SeccionManager, '/api/seccion')
flask.api.add_resource(UsuarioRest.UsuarioManager, '/api/usuario')

if __name__ == '__main__':
    flask.app.run(debug=True)