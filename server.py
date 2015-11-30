from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/<string:name>')
def projects(name):
	return render_template(name)

def init():
	pass

if __name__ == '__main__':
    init()
    app.run(debug=True)