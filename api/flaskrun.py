import flasksetup as flask
import CursoRest
import SeccionRest
import UsuarioRest
import CarreraRest
import GradoRest

flask.api.add_resource(CarreraRest.CarreraManager, '/api/carrera')
flask.api.add_resource(CursoRest.CursoManager, '/api/curso')
flask.api.add_resource(GradoRest.GradoManager, '/api/grado')
flask.api.add_resource(SeccionRest.SeccionManager, '/api/seccion')
flask.api.add_resource(UsuarioRest.UsuarioManager, '/api/usuario')

if __name__ == '__main__':
    flask.app.run(debug=True, host='0.0.0.0', port='9980')