from flask_restful import Resource
from Classes.Database import Database

class IncContadorCagaPau(Resource):
    def get(self):
        db = Database()
        db.update('caga_pau', 'contagem=contagem+1', None)
        rows = db.get('contagem','caga_pau',None)
        idx = 1
        ret = {}
        for row in rows:
            ret[idx] = row[0]
            idx+=1
        return ret
