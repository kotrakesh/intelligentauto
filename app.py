from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def login():
	return render_template('%s.html' % 'login')
@app.route('/workflow')
def workflow():
	return render_template('%s.html' % 'index')#
@app.route('/workflow/recruiting-applet')
def workflowdetail():
	return render_template('%s.html' % 'workflow-detail')
@app.route('/workflow/interview-tracker')
def interviewtrack():
	return render_template('%s.html' % 'interview-tracker')	
@app.route('/dashboard')
def dashbord():
	return render_template('%s.html' % 'dashboard')
if __name__ == '__main__':
    app.run(debug=True)    