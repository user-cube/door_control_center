from flask import Flask, jsonify, render_template, request, redirect
from flask_cors import CORS
import mongo_api

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins":"*"}})
mongo = mongo_api.MongoAPI()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
