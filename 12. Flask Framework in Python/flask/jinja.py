# Building Url Dynamically
# Variable Rule
# Jinja 2 Template Engine


# Jinja2 Template Engine

'''
{{}} Expressions to print output in html
{%...%} conditions, for loops
{#...#} single line comments
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask App</h1></html>"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}!"
    return render_template("form.html")


# Variable rule
# Variable Rule, where we restric a variable to be of a specifice data type
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"

    return render_template("result.html", results=res)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    exp = {'score': score, "res": res}

    return render_template("result1.html", results=exp)


# If condition
@app.route("/successif/<int:score>")
def successif(score):

    return render_template("result2.html", results=score)


# If condition
@app.route("/fail/<int:score>")
def fail(score):

    return render_template("result2.html", results=score)


@app.route("/getresults", methods=["GET", "POST"])
def getresults():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        data_science = float(request.form["data_science"])
        total_score = (science + maths + c+data_science)/4
        return redirect(url_for("successres", score=total_score))
    return render_template("getresults.html")


if __name__ == "__main__":
    app.run(debug=True)
