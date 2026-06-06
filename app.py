from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Heyyy! This is the output which is not printed normally, but from the Python Flask application running on the system."

if __name__ == "__main__":
    app.run(debug=True)
