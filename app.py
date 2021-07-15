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

api.add_resource(Greet, '/greet/<username>')                    #GET
api.add_resource(Birthday, '/birthday/<username>')              #GET
api.add_resource(EvenOdd, '/even_odd')                          #GET
api.add_resource(ContadadorCagaPau, '/contador_caga_pau')       #GET
api.add_resource(IncContadorCagaPau, '/contador_caga_pau++')    #GET
api.add_resource(Meme, '/meme')                                 #GET
api.add_resource(Roll, '/roll')                                 #POST   Params: dados(int), lados(int)
api.add_resource(Calculadora, '/calculadora')                   #POST   Params: number1(float), number2(float), operation(str)
api.add_resource(Primo, '/primo')                               #POST   Params: numbers(str)
api.add_resource(Fatorar, '/fatorar')                           #POST   Params: numbers(str)
api.add_resource(AddMeme, '/add_meme')                          #POST   Params: new_meme(str)

'''
TODO:
api.add_resource(ExportMeme, /export_meme)
'''
