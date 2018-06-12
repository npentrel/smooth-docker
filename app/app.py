from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

## Feel free to change this!
pokemon = {
    'pkdx_id': 1,
    'name': 'Bulbasaur',
    'art_url': 'http://assets22.pokemon.com/assets/cms2/img/pokedex/full/001.png'
}

@app.route('/')
def index():
  return render_template("index.html", pokemon=pokemon)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9000)
