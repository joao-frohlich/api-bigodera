from flask_restful import Resource
from Classes.Database import Database
import random

class Meme(Resource):
    def get(self):
        db = Database()
        memes = db.get('texto_meme','meme',None)
        return {1: random.choice(memes)[0]}
