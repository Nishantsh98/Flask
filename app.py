# Create a simple Flask application

from flask import Flask,request,render_template,jsonify

# create the flask app

app=Flask(__name__)   # object flask

@app.route('/')    # Method
def home():
    return 'hello world'

@app.route('/calculator',methods=["Get"])
def math_operation():
    operation= request.json["operation"]                           # input from postman in the form of json
    num1=request.json["num1"]
    num2=request.json["num2"]

    if operation=='add':
        result=int(num1)+int(num2)
    elif operation=='mul':
        result=int(num1)*int(num2)
    elif operation=='div':
        result=int(num1)/int(num2)
    else:
        result=int(num1)-int(num2)
    
    return jsonify(result)

if __name__=='__main__':
    app.run()