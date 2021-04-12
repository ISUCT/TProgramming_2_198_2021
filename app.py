from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2>Hello, World!</h2>'

@app.route('/current_time')
def c_time():
    return f'Now: {datetime.now()}'
