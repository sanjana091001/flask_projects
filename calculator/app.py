from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def more():
    num1=request.form.get("number1")
    num2=request.form.get("number2")
    num1=int(num1)
    num2=int(num2)
    op=request.form.get("operations")
    if op=='addition':
        num3=num1+num2
    elif op=='subtraction':
        num3=num1-num2
    elif op=='multiplication':
        num3=num1*num2
    else:
        num3=num1/num2
    return render_template("index.html",headline=num3)

    
