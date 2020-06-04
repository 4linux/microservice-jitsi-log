from flaskr import app
from flask import Response, request
from platform import node
from pymongo import MongoClient
from os import getenv
from datetime import datetime


@app.route("/")
def index():
    return Response("microservice-jitsi-log", mimetype="text/plain")


@app.route("/healthcheck")
def healthcheck():
    return Response(
        ("Awake and alive from ", node()), status=200, mimetype="text/plain"
    )


@app.route("/api/v1.0/logs", methods=["POST"])
def addLog():
    data = request.json
    try:
        if "courseid" and "jid" and "displayname" and "action" in data:
            if getenv("URI_MONGODBD"):
                URI = getenv("URI_MONGODBD")
            else:
                URI = "mongodb://localhost:27017/"
            try:
                client = MongoClient(URI)
                db = client["jitsilog"]
                logs = db["logs"]
                insert = {
                    "courseid": data["courseid"],
                    "jid": data["jid"],
                    "displayname": data["displayname"],
                    "timestamp": datetime.utcnow(),
                    "action": data["action"],
                }
                insert["id"] = logs.insert_one(insert).inserted_id
                return Response(str(insert["id"]), status=200, mimetype="text/plain")
            except (AutoReconnect, ConnectionFailure, NetworkTimeout, NotMasterError,ServerSelectionTimeoutError) as e:
                return Response("Falha na conexao com o banco!", status=503, mimetype="text/plain")
            except InvalidURI as e:
                return Response("Erro! URI invalida!", status=500, mimetype="text/plain")
        else:
            return Response("Erro! Falta argumentos!", status=400, mimetype="text/plain")
            app.logger.info('Carga incorreta')
    except TypeError:
        return Response("Erro! Payload JSON nulo!", status=400, mimetype="text/plain")
        app.logger.info('Carga incorreta')
