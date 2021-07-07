from flask_restful import Resource
from Classes.Database import Database

class AddMeme(Resource):
    def get(self, new_meme):
        db = Database()
        try:
            db.insert('meme', 'texto_meme', '\'' + new_meme.replace('_', ' ') + '\'')
            return {1: 'Meme inserido com sucesso'}
        except:
            return {1: 'Falha ao adicionar novo meme ;-;'}
