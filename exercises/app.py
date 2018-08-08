from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#def home_page():
#    return(render_template("index.html"))

def hello_world():
    players = ["reckless","faker","sOAZ"] 
    return render_template("index.html",players=players,
    liked_players = True)


if __name__ == '__main__':
   app.run(debug = True)