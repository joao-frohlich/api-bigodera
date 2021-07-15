from flask_restful import Resource, reqparse
from math import sqrt, gcd
from itertools import count, islice

post_parser = reqparse.RequestParser()
post_parser.add_argument('numbers')

class Primo(Resource):
    def isPrime(self,n):
        if n < 2:
            return False
        for number in islice(count(2), int(sqrt(n) - 1)):
            if n % number == 0:
                return False
        return True

    def isCoprime(self,a,b):
        return gcd(a,b) == 1

    def post(self):
        try:
            numbers = post_parser.parse_args()['numbers'].split(' ')
            if len(numbers) > 2:
                return {1: 'Mano, para de querer me zoar!'}
            elif len(numbers) == 2:
                try:
                    ret = {}
                    x = int(numbers[0])
                    y = int(numbers[1])
                    if (self.isPrime(x)):
                        ret[1] = numbers[0] + ' é primo'
                    else:
                        ret[1] = numbers[0] + ' não é primo'
                    if (self.isPrime(y)):
                        ret[2] = numbers[1] + ' é primo'
                    else:
                        ret[2] = numbers[1] + ' não é primo'
                    if (self.isCoprime(x,y)):
                        ret[3] = numbers[0] + ' e ' + numbers[1] + ' são coprimos'
                    else:
                        ret[3] = numbers[0] + ' e ' + numbers[1] + ' não são coprimos'
                    return ret
                except:
                    return {1: 'Mano, para de querer me zoar!'}
            else:
                x = int(numbers[0])
                try:
                    if (self.isPrime(x)):
                        return {1: numbers[0] + ' é primo'}
                    else:
                        return {1: numbers[0] + ' não é primo'}
                except:
                    return {1: 'Mano, para de querer me zoar!'}
        except:
            return {1: 'Mano, para de querer me zoar!'}
