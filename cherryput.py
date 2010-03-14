#!/usr/bin/python

import cherrypy

class CherryPut:
           
    @cherrypy.expose
    def default(self, *args, **kwargs):
        if cherrypy.request.method == 'PUT':
            fd = open('./' + cherrypy.request.path_info, 'w')
            fd.write(cherrypy.request.body.read())
            fd.close()
            cherrypy.response.status = 201
            cherrypy.response.headers['Location'] = cherrypy.request.path_info
        else:
            cherrypy.response.status = 405

root = CherryPut()
app = cherrypy.tree.mount(root, script_name='/')
cherrypy.quickstart(CherryPut())