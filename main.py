from flask import Flask,render_template      

app=Flask(__name__)

@app.route("/aboutus")
def homepage():
    return render_template("aboutus.html")
@app.route("/")
def indexpage():
    return render_template("home.html")
@app.route("/contact")
def contact():
    return render_template("contactus.html")


if __name__=="__main__":
    app.run(port=1000,debug=True)
