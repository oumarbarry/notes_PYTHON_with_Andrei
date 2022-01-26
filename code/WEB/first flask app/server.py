from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<username>')
def about(username=None, c=None):
   return render_template('index.html', **locals())