from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        print(request.json)
        return "SUCCESS"
    return render_template('index.html')

# @app.route('/')
# def post_user_code():
#     text 
    
if __name__ == "__main__":
    app.run(debug=True)