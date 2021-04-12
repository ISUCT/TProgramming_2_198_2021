from flask import Flask, request
from datetime import datetime
from flask import render_template

app = Flask(__name__)

@app.route('/simple')
def hello_world():
    return '<h2>Hello, World!</h2>'

@app.route('/current_time')
def c_time():
    return f'Now: {datetime.now()}'

@app.route('/')
def base_template():
    name = request.args.get('name', default = "Untitled", type = str)
    user = {
        "name": name
    }
    return render_template('index.html', title="Flask", user=user)

@app.route('/dow')
def dow():
    days = ["Понедельник", 
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
    ]
    return render_template('days.html', days=days)

@app.route('/simple_calc')
def calc():
    a = request.args.get('a', default = 0, type = float)
    b = request.args.get('b', default = 0, type = float)
    res = a + b
    return render_template('simple_calc.html', res=res)