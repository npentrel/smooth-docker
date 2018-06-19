from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

## Feel free to change this!
smoothie = {
    'pkdx_id': 1,
    'name': 'Mixed-Berry',
    'img': 'https://www.maxpixel.net/static/photo/2x/Glass-Healthy-Smoothie-Milkshake-Mixed-Berry-2523597.jpg'
}

@app.route('/')
def index():
    return render_template("index.html", smoothie=smoothie)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
