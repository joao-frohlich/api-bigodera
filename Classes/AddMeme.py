from flask_restful import Resource, reqparse
from Classes.Database import Database

post_parser = reqparse.RequestParser()
post_parser.add_argument('new_meme')

class AddMeme(Resource):
    def post(self):
        db = Database()
        try:
            db.insert('meme', 'cod_meme, texto_meme', '1, \'' + post_parser.parse_args()['new_meme'] + '\'')
            return {1: 'Meme inserido com sucesso'}
        except:
            return {1: 'Falha ao adicionar novo meme ;-;'}
