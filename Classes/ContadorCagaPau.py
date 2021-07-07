from flask_restful import Resource
from Classes.Database import Database

class ContadadorCagaPau(Resource):
    def get(self):
        db = Database()
        rows = db.get('*', 'caga_pau', None)
        idx = 1
        ret = {}
        for row in rows:
            ret[idx] = row[0]
            idx+=1
        return ret
