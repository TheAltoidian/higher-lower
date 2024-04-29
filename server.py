from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def lander():
    return ("<p>Guess a number between 0 and 9</p>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>")

@app.route("/<int:number>")
def guess(number):
    global answer
    if number > answer:
        return ("<h1 style='color:blue'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>")
    elif number < answer:
        return ("<h1 style='color:red'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>")
    else:
        return ("<h1 style='color:green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>")

answer = randint(1,9)
if __name__ == "__main__":
    print(answer)
    app.run()