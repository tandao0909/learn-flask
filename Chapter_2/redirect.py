from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://www.example.com")