from jinja2 import Environment
from jinja2 import FileSystemLoader

from wsgiref.simple_server import make_server

def application(env, start_responde):
    headers = [ ('Content-Type', 'text/html')]
    
    start_responde('200 OK', headers)
    
    env = Environment(loader=FileSystemLoader('templates'))
    
    template =env.get_template('index.html')
    
    html = template.render(
        {
            'tittle': 'Servidor en Python',
            'name': 'Alberto'
        }
    )
    
    return [bytes(html, 'utf-8')]
    
server = make_server('localhost',8000, application )
server.serve_forever()