from flask import Flask
from flask_restful import Api

from Classes.Greet import Greet
from Classes.EvenOdd import EvenOdd
from Classes.Roll import Roll
from Classes.Birthday import Birthday
from Classes.Calculadora import Calculadora
from Classes.Primo import Primo
from Classes.Fatorar import Fatorar
from Classes.ContadorCagaPau import ContadadorCagaPau
from Classes.IncContadorCagaPau import IncContadorCagaPau
from Classes.Meme import Meme
from Classes.AddMeme import AddMeme

app = Flask(__name__)
api = Api(app)

api.add_resource(Greet, '/greet/<username>')
api.add_resource(EvenOdd, '/even_odd')
api.add_resource(Roll, '/roll/<int:dados>/<int:lados>')
api.add_resource(Birthday, '/birthday/<username>')
api.add_resource(Calculadora, '/calculadora/<x>/<op>/<y>')
api.add_resource(Primo, '/primo/<xs>')
api.add_resource(Fatorar, '/fatorar/<numbers>')
api.add_resource(ContadadorCagaPau, '/contador_caga_pau')
api.add_resource(IncContadorCagaPau, '/contador_caga_pau++')
api.add_resource(Meme, '/meme')
api.add_resource(AddMeme, '/add_meme/<new_meme>')

'''
TODO:
api.add_resource(ExportMeme, /export_meme)
'''
