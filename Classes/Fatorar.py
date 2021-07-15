from flask_restful import Resource, reqparse

post_parser = reqparse.RequestParser()
post_parser.add_argument('numbers')

class Fatorar(Resource):
    def verify_integer(self, x):
        try:
            int(x)
            return True
        except ValueError:
            return False
    def factorization(self, x):
        ans = ''
        aux = 3
        while (x > 1):
            if (not x%2):
                ans += '2 '
                x = x//2
                continue
            else:
                flag = False
                for i in range(aux,int(x**(1/2))+1,2):
                    if (not x%i):
                        ans += str(i) + ' '
                        x = x//i
                        aux = i
                        flag = True
                        break
                if not flag:
                    ans += str(x) + ' '
                    break
        ans = ans[:len(ans)-1]
        return ans
    def post(self):
        args = post_parser.parse_args()
        try:
            numbers = [int(x) for x in args['numbers'].split(' ')]
            print(numbers)
            if len(numbers) <= 10 and len(numbers) > 0:
                ret = {}
                idx = 1
                for number in numbers:
                    # print(number)
                    text = ''
                    if not self.verify_integer(number):
                        text += number+' é estranho, me parece arriscado fatorar'
                    else:
                        number = int(number)
                        if (number < 1):
                            text += str(number)+' é estranho, me parece arriscado fatorar'
                        elif (number == 1):
                            text += '1: 1'
                        elif (number > 2**50):
                            text += str(number)+' é muito grande pra mim'
                        else:
                            text += str(number)+': ' + self.factorization(number)
                    ret[idx] = text
                    idx+=1
                # print(ret)
                return ret
            else:
                return {1: 'Não exagera também'}
        except:
            return {1: 'Algo de errado nao esta certo'}
