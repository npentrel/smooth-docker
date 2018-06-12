from flask import Flask, render_template
from pymongo import MongoClient
import random

client = MongoClient("mongodb://database:27017")
app = Flask(__name__, static_url_path='')

def get_pokemon(id):
    return client.test.pokemon.find_one({'pkdx_id': id})

def get_5_random_pokemon():
    arr = []
    for i in range(5):
        arr.append(get_pokemon(random.randint(1,151)))
    return arr

@app.route('/')
def index():
  results = get_5_random_pokemon()
  return render_template("index.html", results=results)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9000)
