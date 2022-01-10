from logging import debug
from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [ 
    { 
        'id': 1, 
        'title': u'Buy groceries', 
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False 
    }, 
    { 
        'id': 2, 
        'title': u'Learn Python', 
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False 
    } 
]

@app.route('/')
def hello():
    return 'hello world'

@app.route('/student')
def hello1():
    return 'hello student'

@app.route('/task')
def hello2():
    return tasks

@app.route('/addtask',methods = ['POST'])
def hello3():
    if not request.json:
        return jsonify({
            "status":"error", 
            "message":"please provide the data"
        },400)

    task = {
        'id': tasks[-1]['id']+1, 
        'title': request.json['title'], 
        'description': request.json.get('description',""), 
        'done': False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"taskadded"
    })

@app.route('/get-task')
def hello4():
    return jsonify({
        "data":tasks
    })

if(__name__ == '__main__'):
    app.run(debug = True)

