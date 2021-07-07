from flask_restful import Resource
from math import log, gcd

class Calculadora(Resource):
    def get(self, x, op, y):
        try:
            number1 = float(x)
            number2 = float(y)
            operation = op
            text = ''
            if operation=='+':
                text = number1+number2
            elif operation=='-':
                text = number1-number2
            elif operation=='*':
                text = number1*number2
            elif operation=='fdiv':
                if number2==0:
                    text = "Você quebrou as regras!"
                else:
                    text = number1/number2
            elif operation=='idiv':
                if number2==0:
                    text = 'Você quebrou as regras!'
                else:
                    text = number1//number2
            elif operation=='xor':
                text = int(number1)^int(number2)
            elif operation=='and':
                text = int(number1)&int(number2)
            elif operation=='or':
                text = int(number1)|int(number2)
            elif operation=='**':
                text = number1**number2;
            elif operation=='mod':
                text = number1%number2
            elif operation=='log':
                text = log(number2, number1)
            elif operation=='gcd':
                number1 = int(number1)
                number2 = int(number2)
                text = gcd(number1, number2)
            else:
                text = 'hummm, n entendi'
        except:
            text = 'hummm, n entendi'
        return {1: text}
