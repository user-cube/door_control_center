from flask import Flask, jsonify, render_template
from flask_cors import CORS
import mongo_api
import home

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins":"*"}})
mongo = mongo_api.MongoAPI()
paths = home.Home.home(app)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template("home.html", paths=paths)

@app.route('/acessos')
def all():
    return jsonify(mongo.getAllCards())

@app.route('/acessos/<home>')
def acessos(home):
    return jsonify(mongo.getCards(home=home))

@app.route('/isValid/<home>/<id>')
def isValid(home, id):
    return mongo.getSpecificCard(home=home, id=id)


if __name__ == '__main__':
    app.run()
