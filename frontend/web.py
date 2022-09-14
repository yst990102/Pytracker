from io import StringIO
import itertools
import os
from flask import Flask, render_template, request
import traceback, subprocess

import sys
import pathlib
import builtins
from yapf.yapflib.yapf_api import FormatFile, FormatCode

backend_absolute_path = str(
    pathlib.Path(__file__).resolve().parents[1]) + "/backend"
frontend_absolute_path = str(
    pathlib.Path(__file__).resolve().parents[1]) + "/frontend"
sys.path.insert(0, backend_absolute_path)

import my_trace
import Pytracker
import feedback_email

app = Flask(__name__, template_folder=frontend_absolute_path + '/templates/')

def input(__prompt: object = ...) -> str:
	userinput = next(userinput_iter)
	return userinput['userinput']

@app.route('/userinput', methods=["POST"])
def get_userinput_list():
    if request.method == "POST":
        global userinput_iter, userinput_list
        userinput_list = request.json
        userinput_iter = iter(request.json)
        
        return {"receive_status": True}
    return render_template('index.html')

@app.route('/traceback', methods=["POST"])
def traceback_checking():
    if request.method == "POST":
        usercode = request.json
        reformatted_code, changed = FormatCode(unformatted_source=usercode, style_config=f"{backend_absolute_path}/.style.yapf")
        
        with open(backend_absolute_path + '/UserCode.py', 'w') as f_write:
            f_write.write(reformatted_code)
        f_write.close()
        
        
        # tracebacke v1.0
        # traceback_result = subprocess.Popen(['python '+ backend_absolute_path + '/UserCode.py'], stderr=subprocess.PIPE, shell=True).stderr.read().decode("utf-8")
        
        input_cmd = []
        for userinput in userinput_list:
            input_cmd.append(userinput['userinput'])
        
        # tracebacke v1.1
        traceback_subprocess = subprocess.Popen(['python '+ backend_absolute_path + '/UserCode.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        
        output, err = traceback_subprocess.communicate(input='\n'.join(input_cmd).encode())
        output_msg = output.decode('utf-8')
        err_msg = err.decode('utf-8')
        print(f"err_msg = {err_msg}")
        if err_msg:
            return {'error': True, 'error_msg': err_msg}
        else:
            return {'error': False}
    return render_template('index.html')


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":

        # run backend_main
        Pytracker.backend_main(usercode=request.json, userinput_iter=userinput_iter)

        # grab the result of listoflist and step_json from global variables
        listoflist = Pytracker.listoflist
        step_json = Pytracker.step_json
        reformatted_code = Pytracker.reformatted_code

        return {'step_json': step_json, 'code': reformatted_code}
    return render_template('index.html')


@app.route('/feedback', methods=["POST"])
def submit_feedback():
    feedback_email.feedback_info = request.json
    email_send_result = feedback_email.send_email()
    if email_send_result == feedback_email.Failed:
        print("feedback email send Failed!!!")
    return render_template('index.html')


@app.route('/input', methods=["POST"])
def user_input():
    if request.method == "POST":
        user_input_content = request.json
        print(f"frontend userinput = {user_input_content}")
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
