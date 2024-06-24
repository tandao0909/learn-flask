from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

# You can omit @app.route('/') and instead use
# app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello {name}</h1>"
