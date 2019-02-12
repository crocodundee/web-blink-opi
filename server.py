import os, os.path
import cherrypy


# --- Jinja2 config
from jinja2 import FileSystemLoader, Environment
file_loader = FileSystemLoader("../webOpi")
env = Environment(loader = file_loader)
template = env.get_template("template/index.html")

# --- Led config
import led
led = Led(port.PA12)

class OpiServer(object):
    @cherrypy.expose
    def index(self):
        return template.render(result="Click the button")

    @cherrypy.expose
    def ledControl(self, ledState):
        if ledState == 'ON':
            action = "Light is on"
            led.lightOn()
        else:
            action = "Light is off"
            led.lightOff()
        return template.render(result = action)

    @cherrypy.expose
    def reset(self, reset):
        return template.render(result="Click the button")

if __name__ == "__main__":
    config = {
        '/style':
            {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'D:\python\webOpi\style'
            }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(OpiServer(), '/', config=config)