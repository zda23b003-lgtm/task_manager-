from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify ({
    'message': 'Welcome to Task Manager API',
    'status': 'running'
    })

@app.route('/hello')
def hello():
    return jsonify ({
    'message': 'Hello, World!'})
@app.route('/api/info')
def info():
    return jsonify ({
    'app_name': 'Task Manager',
    'version': '1.0',
    'author': 'omsekhar'
    })

@app.route('/api/status')
def status():
    return jsonify ({
    'database': 'connected',
    'server': 'running',
    'uptime': '24 hours'
    })
@app.route('/api/greet')
def greet():
    name = request.args.get('name','Guest')

    return jsonify ({
    'message': f'Hello, {name}!',
    'greeting': 'Welcome to Task Manager'
    })
def add():
    a=request.args.get('a',1)
    b=request.args.get('b',2)
    a=int(a)
    b=int(b)
    c=a+b

    return jsonify ({'results':c})
if __name__ == '__main__':
    app.run(debug=True, port=5000)