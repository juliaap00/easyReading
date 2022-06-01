from flask import Flask,jsonify,request, render_template, make_response
from modules.utils.periphrasisSimplifier  import periphrasisSimplifier

app = Flask(__name__)

@app.route('/easyReading', methods = ['GET', 'POST'])
def index():    
    return render_template('index.html', outputText='')


@app.route('/simplifyPeriphrasis', methods = ['GET'])
def simplifyPeriphrasis():
    data = request.args
    if not data:
        return render_template('index.html', outputText='')

    simplified = ''
    sourceText = data.get('sourceText')
    periphrasisList = request.args.get('list')
    json = periphrasisSimplifier(sourceText, periphrasisList)
    print(json)
    render_template('index.html',  outputText=json)
    return jsonify(json)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

