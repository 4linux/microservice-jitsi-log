from flask import Flask, jsonify, Response, request
from pymongo import MongoClient
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def index():
    return Response("microservice-jitsi-log", mimetype="text/plain")


@app.route("/healthcheck")
def healthcheck():
    return Response("Awake and alive", status=200, mimetype="text/plain")


@app.route("/api", methods=["POST"])
def addLog():
    data = request.json
    if "jid" and "displayname" and "timestamp" and "action" in data:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["jitsilog"]
        logs = db["logs"]
        insert = {
            "jid": data["jid"],
            "displayname": data["displayname"],
            "timestamp": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
            "action": data["action"],
        }
        insert['id'] = logs.insert_one(insert).inserted_id
        return  Response(str(insert['id']), status=200, mimetype='text/plain')
    else:
        return Response("Error!", status=400, mimetype='text/plain')
