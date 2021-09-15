# API Bigodera

## Overview
This is a simple python API created with the initial purpose to centralize the actions performed in common by the two bots created by members of the [BRUTE Competitive Programming](bruteudesc.com) for [Discord](https://github.com/EMachad0/BigoderaDiscord-Bot) and [Telegram](https://github.com/VGasparini/bigodera-bot).

Currently, the API is hosted on [Heroku](https://api-bigodera.herokuapp.com/). While the given URL gives a 404 response, you can see how to use in the following section

## Usage
To use the bot, you have to create requests according to the methods of each function, as it is listed below:

```
https://api-bigodera.herokuapp.com/greet/<username>     (GET) Greets you according to the <username> provided
https://api-bigodera.herokuapp.com/birthday/<username>  (GET) Wishes <username> a happy birthday
https://api-bigodera.herokuapp.com/even_odd             (GET) Returns even or odd, just like a coin flip
https://api-bigodera.herokuapp.com/contador_caga_pau    (GET) Retrieves the number of times someone in the BRUTE has done some several mistake
https://api-bigodera.herokuapp.com/contador_caga_pau++  (GET) Increases the counter by 1
https://api-bigodera.herokuapp.com/meme                 (GET) Retrieves a random meme phrase from the database with some internal joke of the BRUTE
https://api-bigodera.herokuapp.com/roll                 (POST | Params: dados(int), lados(int)) Rolls dados dice of lados faces
https://api-bigodera.herokuapp.com/calculadora')        (POST | Params: number1(float), number2(float), operation(str)) Performs the operation with number1 and number2. The operations will be listed in another section.
https://api-bigodera.herokuapp.com/primo')              (POST | Params: numbers(str)) Verifies if the numbers (must be at most 2 numbers) given in the string in the format "x1 x2" are primes and/or coprime
https://api-bigodera.herokuapp.com/fatorar')            (POST | Params: numbers(str)) Factorates a list of numbers (must be at most 10 numbers) given in a string in the format "x1 x2 ... x10"
https://api-bigodera.herokuapp.com/add_meme')           (POST | Params: new_meme(str)) Insert the new_meme in the database
https://api-bigodera.herokuapp.com/cfproblem')          (POST | Params: rating(int), tags(str), id_telegram(int), id_discord(int)) Get a random codeforces problem with the given rating and tags that user with the handle that belongs to the given id_telegram or id_discord (you can use one of them in each call) haven't solved yet
https://api-bigodera.herokuapp.com/user')               (POST | Params: handle(str), id_telegram(int), id_discord(int)) This function insert the handle in the database, if the handle wasn't inserted yet, or assign an id_telegram or id_discord to the inserted handle. One id_telegram and id_discord can be assigned to only one handle and one handle can belong to one id_telegram and one id_discord.
https://api-bigodera.herokuapp.com/del_user')           (DELETE | Params: id_telegram(int), id_discord(int) Delete the handle from the database
```

The response to every call will be a JSON with one or more lines, each one containing an Integer from 1 to number of lines as a key, and a string with the result of the function called. Every GET method can be used in the browser, with the possibility to change \<username\> by any name you want in the greet and birthday functions.

Currently, neither the Telegram bot nor the Discord bot are officialy using the API, besides there is a version of the Telegram bot with the modifications needed to use the API, but it's currently not merged on the deployment repository.
  
### Calculadora function operations

Here is the list of operations supported by the function until now

```
"+": number1 + number2
"-": number1 - number2
"*": number1 * number2
"/": number1 / number2
"//": int(number1 / number2)
"^": number1 (xor) number2
"&": number1 (and) number2
"|": number1 (or) number2
"**": number1 ** number2
"%": number1 % number2
"log": logarithm of number1 on base number2
"gcd": greatest common divisor of number1 and number2
```

## Developing the project

First of all, remember to create branches to modify code, and after you have made the modifications and tested it, submit a pull request, that will be validated.

This instructions are for Linux users

The development of this API runs on a python virtual enviroment (if you don't know what is a python virtual enviroment, I suggest you to read [this article](https://www.geeksforgeeks.org/python-virtual-environment/)), which uses the version 3.8.10 of python.  

After cloning this repository, you can access the pyenv with the command:  
`source venv/bin/activate`

To install all the python packages required to run this project, run (on the pyenv):
`pip install -r requirements.txt`

After installing all the packages, you need to create a postgresql database. The script for creating the database is in the file db_creation.sql. Remember to modify the values in the configure.env file.

After setting up the database, you need to setup some enviroment variables in order to run the application. For this purpose, I created the shell script configure.sh. Run the script with:
`./configure.sh`

And finally, you can run the application with:
`flask run`

With this, you are able to test the program and every modification you make.  
If you want more information about how the code works, I suggest the documentation of [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/).

If there are any questions, you can contact me on [Telegram](https://t.me/joaofrohlich)
