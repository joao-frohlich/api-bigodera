from flask_restful import Resource
import random

class Birthday(Resource):
    def get(self, username):
        textos = ['Feliz aniversario, {}! Te amooo', 'Faaaala {}. parabéns cara \'-\'', 'Oi {}. Parabéns. Paga uma pizza pra nois', 'Hoje é seu dia, que dia mais feliz... Parabens {}']
        return {1: random.choice(tuple(textos)).format(username.capitalize())}
