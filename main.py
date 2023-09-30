from flask import Flask, render_template, Response
import csv

app = Flask(__name__)

@app.route("/")
def hello_page():
    return render_template('index.html')

@app.route("/stat")
async def get_data():
    pass

if __name__ == "__main__":
    app.run(debug=True)