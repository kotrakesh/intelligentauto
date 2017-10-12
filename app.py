from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hellworld():
	return render_template('%s.html' % 'login')

@app.route('/dashboard')
def hello_world():
	return render_template('%s.html' % 'index')
if __name__ == '__main__':
    app.run(debug=True)    