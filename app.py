from flask import Flask, render_template, request
from chatbot import simple_chatbot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        query = request.form["query"]
        company = request.form["company"]
        year = int(request.form["year"])
        response = simple_chatbot(query, company, year)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
