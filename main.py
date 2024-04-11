from flask import Flask,render_template , request,redirect,flash
# import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os






# conn = mysql.connector.connect(host = "localhost", username = "root", password = "0121", database = "flaskdata")

# curser = conn.cursor()

app=Flask(__name__)
app.secret_key = "askdjaskdbkjasbdkjbasdbasdbasjkbaskbsabdsajdbjkasbdakjdb"


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db=SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'creative07vibez@gmail.com'
app.config['MAIL_PASSWORD'] = 'mvoc yrpg bkzq erii'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 






class contactus(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(120))
    MSG=db.Column(db.Text)
    myimage = db.Column(db.String(255))
with app.app_context():
 db.create_all()



@app.route("/aboutus")
def homepage():
    return render_template("aboutus.html")
@app.route("/")
def indexpage():
    return render_template("home.html")
@app.route("/contact")
def contact():
    return render_template("contactus.html")
@app.route("/services")
def services():
    data = contactus.query.all()
    return render_template("services.html",data=data)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = contactus.query.get(id)
    return render_template("update.html",udata=data)

@app.route("/savedata", methods =["post"])
def savedata():
    if request.method=="POST" :
      title=request.form.get("title")
      msg=request.form.get("msg")
      myimg=request.files.get("img")
      if myimg:
        myimg.save(os.path.join("static/images", myimg.filename))
        path = os.path.join("static/images", myimg.filename)


      data=contactus(Title=title,MSG=msg, myimage = path)
      db.session.add(data)
      db.session.commit()
      msg = Message(subject='Hello from the other side!', sender='creative07vibez@gmail.com', recipients=['rohitpatial121@gmail.com'])
      msg.body = "Hey Rohit, sending you this email from my Flask app, lmk if it works"
      mail.send(msg)
    #   curser.execute(f"insert into pets values('{title}', '{msg}')")
    #   conn.commit()

      flash("Data saved sucessfully..............")
      return redirect("/contact")




@app.route("/delete/<int:id>", methods=["POST"])
def user_delete(id):
    user = contactus.query.get(id)
    # user = contactus.query.filter_by(id=x).first()
    db.session.delete(user)
    db.session.commit()
    return redirect("/services")


@app.route("/updatethis/<int:id>", methods=["POST"])
def update_this(id):
   if request.method=="POST" :
          title=request.form.get("title")
          msg=request.form.get("msg")
          user = contactus.query.get(id)
          user.Title=title
          user.MSG=msg
          db.session.commit()
          return redirect("/services")

if __name__=="__main__":
    app.run(port=1000,debug=True)
