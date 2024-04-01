from flask import Flask,render_template , request    

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

@app.route("/savedata", methods =["post"])
def savedata():
    if request.method=="POST" :
      title=request.form.get("title")
      msg=request.form.get("msg")
      print(title,msg)
      return "data saved "


if __name__=="__main__":
    app.run(port=1000,debug=True)
