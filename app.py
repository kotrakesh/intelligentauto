from flask import Flask, render_template,request,make_response
import json
app = Flask(__name__)

@app.route('/')
def login():
	return render_template('%s.html' % 'login')
@app.route('/workflow')
def workflow():
	return render_template('%s.html' % 'index')#
@app.route('/domains')
def domains():
	return render_template('%s.html' % 'domains')#
@app.route('/logistics')
def logistics():
	return render_template('%s.html' % 'logistics')#
@app.route('/finances')
def finances():
	return render_template('%s.html' % 'finances')#
@app.route('/workflow/recruiting-applet')
def workflowdetail():
	return render_template('%s.html' % 'workflow-detail')
@app.route('/workflow/interview-tracker')
def interviewtrack():
	return render_template('%s.html' % 'interview-tracker')	
@app.route('/dashboard')
def dashbord():
	return render_template('%s.html' % 'dashboard')
@app.route('/loginservice', methods=['GET', 'POST'])	
def loginservice():
	ret='False'
	if(request.form['username']=="hradmin" and request.form['password']=="admin123"):
		ret=make_response('True')
		ret.set_cookie('username', 'hradmin')
	return ret
if __name__ == '__main__':
    app.run(debug=True)    