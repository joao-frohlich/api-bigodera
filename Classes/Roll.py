from flask_restful import Resource
import random

class Roll(Resource):
    def get(self, dados, lados):
        if (dados > 100):
            return {1: 'Vsf! Porrada de Dado.'}
        else:
            ret = {}
            for i in range(1,dados+1):
                ret[i] = random.randrange(lados)+1
            return ret
