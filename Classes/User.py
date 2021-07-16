from flask_restful import Resource, reqparse
from Classes.Database import Database

post_parser = reqparse.RequestParser()
post_parser.add_argument('handle')
post_parser.add_argument('id_discord')
post_parser.add_argument('id_telegram')

class User(Resource):
    def post(self):
        args = post_parser.parse_args()
        db = Database()
        try:
            if args['id_discord'] != None:
                existent_id = db.get('id_discord', 'usuario', 'id_discord = ' + args['id_discord'])
                if existent_id != []:
                    return {1: 'ID Discord ja cadastrado'}
                existent_user = db.get('handle, id_discord', 'usuario', 'handle = \'' + args['handle'] + '\'')
                if existent_user == []:
                    db.insert('usuario', 'cod_usuario, handle, id_discord', '1, \''+args['handle']+'\', ' + str(int(args['id_discord'])))
                    return {1: 'Usuario inserido com sucesso'}
                elif existent_user[0][1] == None:
                    db.update('usuario', 'id_discord = ' + str(int(args['id_discord'])), 'handle = \'' + args['handle'] + '\'')
                    return {1: 'Id Discord associado ao handle ' + args['handle']}
                else:
                    return {1: 'Usuario ja cadastrado'}
            elif args['id_telegram'] != None:
                existent_id = db.get('id_telegram', 'usuario', 'id_telegram = ' + args['id_telegram'])
                if existent_id != []:
                    return {1: 'ID Telegram ja cadastrado'}
                existent_user = db.get('handle, id_telegram', 'usuario', 'handle = \'' + args['handle']  + '\'')
                if existent_user == []:
                    db.insert('usuario', 'cod_usuario, handle, id_telegram', '1, \''+args['handle']+'\', ' + str(int(args['id_telegram'])))
                    return {1: 'Usuario inserido com sucesso'}
                elif existent_user[0][1] == None:
                    db.update('usuario', 'id_telegram = ' + str(int(args['id_telegram'])), 'handle = \'' + args['handle'] + '\'')
                    return {1: 'Id Telegram associado ao handle ' + args['handle']}
                else:
                    return {1: 'Usuario ja cadastrado'}
            else:
                return {1: 'Falha ao cadastrar usuario'}
        except:
            return {1: 'Falha ao cadastrar usuario'}
