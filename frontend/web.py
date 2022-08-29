from flask import Flask, render_template, request

import sys
import pathlib
backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())
sys.path.insert(0, backend_absolute_path + "/backend")

import Pytracker
import feedback_email

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":

        # run backend_main
        Pytracker.backend_main(usercode=request.json)

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

if __name__ == "__main__":
    app.run(debug=True)
