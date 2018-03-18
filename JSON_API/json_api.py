from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)

@app.route('/json_api', methods = ['GET'])
def json_api():


    if 'input' in request.args:
        inputdata = request.args['input']

    try:
        int(inputdata)
    except ValueError:
        responsecode = 'acki'
    else:
        responsecode ='acks'


    response = {
        'Input':inputdata,
        'Response':responsecode
    }

    js = json.dumps(response)
    return js

if __name__ == '__main__':
    app.run(debug=True)
