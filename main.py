from flask import Flask,render_template , request,redirect
import mysql.connector

conn = mysql.connector.connect(host = "localhost", username = "root", password = "0121", database = "flaskdata")

curser = conn.cursor()

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
      curser.execute(f"insert into pets values('{title}', '{msg}')")
      conn.commit()
      return redirect("/contact")



if __name__=="__main__":
    app.run(port=1000,debug=True)
