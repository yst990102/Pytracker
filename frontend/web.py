from flask import Flask, render_template, request
import os
import backend.Pytracker as Pytracker

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        # write usercode to backend test_script_file
        with open("../backend/UserCode.py", 'w') as usercode_w:
            usercode_w.write(request.json)
        usercode_w.close()
        
        # run backend_main()
        Pytracker.backend_main()
        
        # grab the result of listoflist and step_json from global variables
        listoflist = Pytracker.listoflist
        step_json = Pytracker.step_json

        return step_json
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)