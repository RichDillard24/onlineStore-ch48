from flask import Flask, request
import json

#globalVariables
items = []
#
app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this is a test"

@app.get("/api/about")
def about():
    me = {"name":"Richard Dil"}
    return json.dumps(me)

@app.post("/api/products")
def saveProduct():
    product = request.get_json()
    print (product)
    items.append(product)
    return json.dumps(product)



@app.get("/api/products")
def getProduct():
    return json.dump(items)




app.run(debug = True ) 