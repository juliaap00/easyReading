from flask import Flask, request
from flask import render_template
from nlp import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', outputText="")


@app.route('/index', methods = ['POST', 'GET'])
def post_text():
   ''' text = request.form['sourceText'] #esto es el json
    return render_template('index.html', outputText=analyze(text))
    '''
    return render_template('index.html', outputText="")
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
