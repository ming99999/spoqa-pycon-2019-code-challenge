from flask import Flask, render_template
from flask_misaka import Misaka

app = Flask(__name__, template_folder = "views")
Misaka(app)

content = ""
with open('event.md', 'r') as f:
    content = f.read()

@app.route("/")
def index():
    return render_template('index.html', text = content)

if __name__ == "__main__":
    app.run(debug = True)
