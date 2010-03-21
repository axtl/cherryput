#!/usr/bin/python

import os

import cherrypy

class CherryPut:
           
    @cherrypy.expose
    def default(self, *args, **kwargs):
        if cherrypy.request.method == 'PUT':
            putpath = './' + cherrypy.request.path_info
            pathlist = putpath.rsplit('/', 1)
            dirs = pathlist[0] if pathlist[0] else '.'
            fname = pathlist[1]
            if not os.path.isdir(dirs):
                os.makedirs(dirs)
            fd = open(putpath, 'w')
            fd.write(cherrypy.request.body.read())
            fd.close()
            cherrypy.response.status = 201
            cherrypy.response.headers['Location'] = cherrypy.request.path_info
        else:
            cherrypy.response.status = 405

root = CherryPut()
app = cherrypy.tree.mount(root, script_name='/')
cherrypy.quickstart(CherryPut())
