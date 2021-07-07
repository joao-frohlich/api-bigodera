from flask_restful import Resource
import random

class Greet(Resource):
    def get(self, username):
        pre = ["E ai ", "Opa ", "Olá ", "Oie ", "Turu bom "]
        suf = ["pro URI", "pro RU", "pro codeforces", "pro code", "pra maratona"]
        return {1: random.choice(pre) + username + ', bem vindo ao BRUTE. Eu sou o Bigodera, o bot dessa galera. Bora ' + random.choice(suf)}
