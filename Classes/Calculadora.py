from flask_restful import Resource, reqparse
from math import log, gcd

post_parser = reqparse.RequestParser()
post_parser.add_argument('number1')
post_parser.add_argument('number2')
post_parser.add_argument('operation')

class Calculadora(Resource):
    def post(self):
        try:
            args = post_parser.parse_args()
            number1 = float(args['number1'])
            number2 = float(args['number2'])
            operation = args['operation']
            text = ''
            if operation=='+':
                text = number1+number2
            elif operation=='-':
                text = number1-number2
            elif operation=='*':
                text = number1*number2
            elif operation=='/':
                if number2==0:
                    text = "Você quebrou as regras!"
                else:
                    text = number1/number2
            elif operation=='//':
                if number2==0:
                    text = 'Você quebrou as regras!'
                else:
                    text = number1//number2
            elif operation=='^':
                text = int(number1)^int(number2)
            elif operation=='&':
                text = int(number1)&int(number2)
            elif operation=='|':
                text = int(number1)|int(number2)
            elif operation=='**':
                text = number1**number2;
            elif operation=='%':
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
