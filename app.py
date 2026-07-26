from flask import Flask
app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return "Hello World"

@app.route('/about', methods=["GET"])
def about():
    return "This is about section"

@app.route('/contact', methods=["POST","GET"])
def contact():
    return "This is about contact"

if __name__=="__main__":
    app.run(debug=True)