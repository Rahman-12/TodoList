import flask 
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    todos = ['go to college on time', 'sleep early','smile on wake up']
    return render_template('index.html',todos = todos)



if __name__ == "__main__":
    app.run(debug = True)