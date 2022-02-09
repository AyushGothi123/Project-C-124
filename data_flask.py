from flask import Flask,jsonify,request
app=  Flask(__name__)
print(__name__)

@app.route("/")

def helloworld():
    return "Welcome to api"

contactNos = [{
     "contact":"9874561235",
     "name":"Mohan",
     "done":False,
     "id":1
},
{
     "contact":"9586425315",
     "name":"Mohit",
     "done":False,
     "id":2
},
{
     "contact":"9854661235",
     "name":"Rohit",
     "done":False,
     "id":3
}]
@app.route("/get-data")

def getdata():
    return jsonify({
        "data":contactNos
    })

@app.route("/post-data",methods = ["POST"])

def postdata():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"plz provide the data",

        },400)
    
    data = {
        "contact":request.json.get('contact'," "),

        "name":request.json['name'],

        'done': False,
        'id':contactNos[-1]['id']+1

    }
    contactNos.append(data)
    return jsonify({
        'status':'success',
        "message":"data added successfully",
        'data':contactNos
    })


if (__name__ == "__main__"):
    app.run(debug = True)
