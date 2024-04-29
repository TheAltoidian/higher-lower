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
        return "<h1>Too high, try again!</h1>"
    elif number < answer:
        return "<h1>Too low, try again!</h1>"
    else:
        return "<h1>You found me!</h1>"

answer = randint(1,9)
if __name__ == "__main__":
    print(answer)
    app.run()