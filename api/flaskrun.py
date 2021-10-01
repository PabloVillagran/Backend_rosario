import flasksetup as flask
import CursoRest
import SeccionRest
import UsuarioRest
import CarreraRest
import GradoRest
import AdministrativoRest
import AlumnoRest
import CalificacionRest
import CursoMateriaRest

flask.api.add_resource(AdministrativoRest.AdministrativoManager, '/api/administrativo')
flask.api.add_resource(AlumnoRest.AlumnoManager, '/api/alumno')
flask.api.add_resource(CalificacionRest.CalificacionManager, '/api/calificacion')
flask.api.add_resource(CarreraRest.CarreraManager, '/api/carrera')
flask.api.add_resource(CursoRest.CursoManager, '/api/curso')
flask.api.add_resource(CursoMateriaRest.CursoMateriaManager, '/api/curso_materia')
flask.api.add_resource(GradoRest.GradoManager, '/api/grado')
flask.api.add_resource(SeccionRest.SeccionManager, '/api/seccion')
flask.api.add_resource(UsuarioRest.UsuarioManager, '/api/usuario')

if __name__ == '__main__':
    flask.app.run(debug=True, host='0.0.0.0', port='9980')