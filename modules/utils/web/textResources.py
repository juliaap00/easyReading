from flask import request

@app.route('/text', methods=['POST'])
def simplifyText():
    return (request.form['sourceText'])