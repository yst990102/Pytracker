from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        # cd to backend path
        os.chdir("../backend")
        # write usercode to backend test_script_file
        with open("UserCode.py", 'w') as usercode_w:
            usercode_w.write(request.json)
        usercode_w.close()
        # run the backend Pytracker.py
        os.system("python Pytracker.py")
        
        return "SUCCESS"
    return render_template('index.html')

# @app.route('/')
# def post_user_code():
#     text 
    
if __name__ == "__main__":
    app.run(debug=True)