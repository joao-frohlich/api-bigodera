from flask_restful import Resource, reqparse
from Classes.Database import Database
from urllib.request import urlopen
from json import loads
from random import randint

def get_codeforces_problem(handle, rating, tags):
    correct_tags = ''
    all_tags = {'2-sat', 'binary search', 'bitmasks', 'brute force', 'chinese remainder theory',
                'combinatorics', 'constructive algorithm', 'data strucutres', 'dfs and similar', 'divide and conquer',
                'dp', 'dsu', 'expression parsing', 'fft', 'flows', 'games', 'geometry', 'graph matchings', 'graphs',
                'greedy', 'hashing', 'implementations', 'interactive', 'math', 'matrices', 'meet-in-the-middle',
                'number theory',
                'probabilities', 'schedules', 'shortest paths', 'sortings', 'string suffix strucutures', 'strings',
                'ternary search', 'trees', 'two pointers'}
    for tag in tags:
        if tag in all_tags:
            correct_tags += tag.replace(" ", "%20") + ';'
    problems = []
    solved = []
    if handle != '':
        # print("https://codeforces.com/api/user.status?handle=" + handle)
        with urlopen("https://codeforces.com/api/user.status?handle=" + handle) as url:
            codeforces_data = loads(url.read().decode())
            for submission in codeforces_data['result']:
                if 'verdict' in submission and submission['verdict'] == 'OK':
                    solved.append([submission['problem']['contestId'], submission['problem']['index']])
    # print("https://codeforces.com/api/problemset.problems?tags=" + correct_tags)
    with urlopen("https://codeforces.com/api/problemset.problems?tags=" + correct_tags) as url:
        codeforces_data = loads(url.read().decode())
        for problem in codeforces_data['result']['problems']:
            if 'rating' in problem and problem['rating'] == int(rating):
                problemId = [problem['contestId'], problem['index']]
                if problemId not in solved:
                    problems.append([problem['name'], problem['contestId'], problem['index']])
    if len(problems) == 0:
        raise Exception("No problem found")
    problem = problems[randint(0, len(problems) - 1)]
    return f"https://codeforces.com/contest/{problem[1]}/problem/{problem[2]}"

post_parser = reqparse.RequestParser()
post_parser.add_argument('id_discord')
post_parser.add_argument('id_telegram')
post_parser.add_argument('rating')
post_parser.add_argument('tags')

class CfProblem(Resource):
    def post(self):
        args = post_parser.parse_args()
        db = Database()
        try:
            if (args['rating'] == None):
                return {1: 'Rating não informado'}
            rating = int(args['rating'])
            tags = ''
            if (args['tags'] != None):
                tags = args['rating'].split(' ')
            print('a')
            if args['id_discord'] != None:
                existent_user = db.get('handle', 'usuario', 'id_discord = ' + args['id_discord'])
                if (existent_user == []):
                    return {1: 'Usuario não cadastrado'}
                else:
                    handle = existent_user[0][0]
                    return {1: get_codeforces_problem(handle, rating, tags)}
            elif args['id_telegram'] != None:
                existent_user = db.get('handle', 'usuario', 'id_telegram = ' + args['id_telegram'])
                if (existent_user == []):
                    return {1: 'Usuario não cadastrado'}
                else:
                    handle = existent_user[0][0]
                    return {1: get_codeforces_problem(handle, rating, tags)}
            else:
                return {1: 'Falha ao buscar problema'}
        except:
            return {1: 'Falha ao buscar problema'}
