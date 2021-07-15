from flask_restful import Resource, reqparse
import random

post_parser = reqparse.RequestParser()
post_parser.add_argument('dados')
post_parser.add_argument('lados')

class Roll(Resource):
    def post(self):
        args = post_parser.parse_args()
        try:
            dados = int(args['dados'])
            lados = int(args['lados'])
            if (dados > 100):
                return {1: 'Vsf! Porrada de Dado.'}
            else:
                ret = {}
                for i in range(1,dados+1):
                    ret[i] = random.randrange(lados)+1
                return ret
        except:
            return {1: 'Algo de errado nao esta certo'}
