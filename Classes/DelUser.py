from flask_restful import Resource, reqparse
from Classes.Database import Database

post_parser = reqparse.RequestParser()
post_parser.add_argument('id_discord')
post_parser.add_argument('id_telegram')

class DelUser(Resource):
    def delete(self):
        args = post_parser.parse_args()
        db = Database()
        try:
            if args['id_discord'] != None:
                db.update('usuario', 'id_discord = null', 'id_discord = ' + args['id_discord'])
                return {1: 'Usuario excluido com sucesso'}
            elif args['id_telegram'] != None:
                db.update('usuario', 'id_telegram = null', 'id_telegram = ' + args['id_telegram'])
                return {1: 'Usuario excluido com sucesso'}
            else:
                return {1: 'Falha ao excluir usuario'}
        except:
            return {1: 'Falha ao excluir usuario'}
