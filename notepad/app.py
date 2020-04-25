from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/notepad", methods=["GET","POST"])
def notepad():
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method=="POST":
        note=request.form.get("note")
        session["notes"].append(note)
    return render_template("notepad.html",notes=session["notes"])