import cherrypy

class CherryPut:
           
    @cherrypy.expose
    def default(self, *args, **kwargs):
        if cherrypy.request.method == 'PUT':
            return "LET'S PUT OUT =)"
        else:
            return "NOT PUTTING UP WITH THIS!"

root = CherryPut()
app = cherrypy.tree.mount(root, script_name='/')
cherrypy.quickstart(CherryPut())