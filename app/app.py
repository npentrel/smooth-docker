from flask import Flask, render_template
from pymongo import MongoClient
import random

client = MongoClient("mongodb://database:27017")
app = Flask(__name__, static_url_path='')

def get_ingredient(id):
    return client.test.ingredients.find_one({'_id': id})

def get_5_random_ingredients():
    arr = []
    for i in range(5):
        arr.append(get_ingredient(random.randint(1,20)))
    return arr

@app.route('/')
def index():
    results = get_5_random_ingredients()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
