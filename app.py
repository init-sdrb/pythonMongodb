from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='strongpass',
                        authSource="admin")
    db = client["mydb"]
    return db


class color:
   BOLD = '\033[1m'
   END = '\033[0m'

@app.route('/')
def ping_server():
    return("*****This is a simple landing page created with the help of Flask, a micro web framework of Python. Please browse http://your_machine_ip:5000/contents to view the contents fetched from MongoDB*****")

@app.route('/contents')
def get_stored_contents():
    db=""
    try:
        db = get_db()
        _contents = db.content_tb.find()
        contents = [{"id": content["id"], "name": content["name"], "address": content["address"]} for content in _contents]
        return jsonify({"contents": contents})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
