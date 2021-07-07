from flask_restful import Resource
import random

class EvenOdd(Resource):
    def get(self):
        if (random.randrange(2)):
            return {1: 'Impar'}
        else:
            return {1: 'Par'}
