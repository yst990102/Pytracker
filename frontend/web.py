from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        # write usercode to backend test_script_file
        with open("UserCode.py", 'w') as usercode_w:
            usercode_w.write(request.json)
        usercode_w.close()

        os.system("python Pytracker.py")
        step_json = eval(open("step_json", 'r').read())

        print(f"step_json from backend == {step_json}")

        return step_json
    return render_template('index.html')


# @app.route('/')
# def post_user_code():
#     text

if __name__ == "__main__":
    app.run(debug=True)