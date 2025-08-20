import flask 
from flask import Flask , render_template, request, redirect
import json

app = Flask(__name__)
def load_todo():
    with open("database.json") as file:
        return json.load(file)
    
def save_todos(data):
    with open("database.json","w") as file:
        json.dump(data,file)





@app.route('/')
def index():
    todos = load_todo()
    return render_template('index.html',todos = todos)


@app.route('/add',methods=['POST',"GET"])
def add_task():
    if request.method == "POST":
        task = request.form["addtodo1"]
        todos = load_todo()
        todos.append(task)
        save_todos(todos)
        return redirect('/')
    return "normal site"



if __name__ == "__main__":
    app.run(debug = True)