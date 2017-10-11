from flask import Flask, render_template
from jinja2 import Template
app = Flask(__name__)

@app.route('/')
def hellworld():
	return "hello"

@app.route('/dashboard')
def hello_world():
	return render_template('%s.html' % 'index')
if __name__ == '__main__':
    app.run(debug=True)    