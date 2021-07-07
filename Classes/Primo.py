from flask_restful import Resource
from math import sqrt, gcd
from itertools import count, islice

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

    def get(self, xs):
        xs = xs.split('_')
        if len(xs) > 2:
            return {1: 'Mano, para de querer me zoar!'}
        elif len(xs) == 2:
            try:
                ret = {}
                x = int(xs[0])
                y = int(xs[1])
                if (self.isPrime(x)):
                    ret[1] = xs[0] + ' é primo'
                else:
                    ret[1] = xs[0] + ' não é primo'
                if (self.isPrime(y)):
                    ret[2] = xs[1] + ' é primo'
                else:
                    ret[2] = xs[1] + ' não é primo'
                if (self.isCoprime(x,y)):
                    ret[3] = xs[0] + ' e ' + xs[1] + ' são coprimos'
                else:
                    ret[3] = xs[0] + ' e ' + xs[1] + ' não são coprimos'
                return ret
            except:
                return {1: 'Mano, para de querer me zoar!'}
        else:
            x = int(xs[0])
            try:
                if (self.isPrime(x)):
                    return {1: xs[0] + ' é primo'}
                else:
                    return {1: xs[0] + ' não é primo'}
            except:
                return {1: 'Mano, para de querer me zoar!'}
