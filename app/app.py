from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

## Feel free to change this!
smoothie = {
    '_id': 1,
    'name': 'Layered Rainbow Smoothies',
    'img': 'http://www.bestofvegan.com/wp-content/uploads/2017/05/layered-rainbow-smoothies-by-@artrawpaulina-1st-layer-banana-mango-spirulina-2nd-layer-banana-mango-.jpg',
    'source': 'http://www.bestofvegan.com/vegan-recipe-285/'
}

@app.route('/')
def index():
    return render_template("index.html", smoothie=smoothie)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
