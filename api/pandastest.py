import cherrypy
import pandas as pd
import test

class MyWebService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def testdb(self):
        return 'Running'
        
config = {'server.socket_host':'0.0.0.0', 'server.socket_port': 9980}
cherrypy.config.update(config)
cherrypy.quickstart(MyWebService())