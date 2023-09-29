from flask import Flask

app = Flask('Cheburussia')

@app.route("/")
def hello_page():
    return "<p>Hello, my Dear friends!</p>"


if __name__ == "__main__":
    app.run(debug=True)