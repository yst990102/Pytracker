from flask import Flask, render_template, request
import os
import backend.Pytracker as Pytracker

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":

        # run backend_main()
        Pytracker.backend_main(usercode=request.json)
        
        # grab the result of listoflist and step_json from global variables
        listoflist = Pytracker.listoflist
        step_json = Pytracker.step_json
        reformatted_code = Pytracker.reformatted_code

        return {
            'step_json': step_json,
            'code': reformatted_code
        }
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)