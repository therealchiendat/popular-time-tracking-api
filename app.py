from flask import Flask, jsonify

import sys
sys.path.insert(0, './scripts')

import mainscript


app = Flask(__name__)


@app.route('/api/stores',methods=['GET'])
def index():
    result = mainscript.app()
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='localhost', port=8080,debug=True)
