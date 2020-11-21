#テンプレートの継承
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Hoge", message="Fuga")

app.run()