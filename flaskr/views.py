from platform import node
from os import getenv
from datetime import datetime

from flask import Response, request, jsonify
from pymongo import MongoClient, errors

from flaskr import app


@app.route("/")
def index():
    return Response("microservice-jitsi-log", status=200, mimetype="text/plain")


@app.route("/healthcheck")
def healthcheck():
    return Response(
        ("Awake and alive from ", node()), status=200, mimetype="text/plain"
    )


@app.route("/v1/logs", methods=["POST"])
def addLog():
    data = request.json
    try:
        if getenv("REQUIRED_FIELDS"):
            fields = (
                getenv("REQUIRED_FIELDS").replace("'", "").replace('"', "").split(",")
            )
        else:
            fields = ["sala", "email", "timestamp", "action"]
        if all(elem in data.keys() for elem in fields):
            if getenv("URI_MONGODB"):
                URI = getenv("URI_MONGODB")
            else:
                URI = "mongodb://localhost:27017/"
            if getenv("DATABASE"):
                DATABASE = getenv("DATABASE")
            else:
                DATABASE = "jitsilog"
            if getenv("COLLECTION"):
                COLLECTION = getenv("COLLECTION")
            else:
                COLLECTION = "logs"
            try:
                client = MongoClient(URI)
                db = client[DATABASE]
                collection = db[COLLECTION]
                data["id"] = collection.insert_one(data).inserted_id
                client.close()
                return jsonify(id=str(data["id"])), 201
            except (
                errors.AutoReconnect,
                errors.ConnectionFailure,
                errors.NetworkTimeout,
                errors.NotMasterError,
                errors.ServerSelectionTimeoutError,
            ) as e:
                return (
                    jsonify(erro="Falha na conexao com o banco!", exception=str(e)),
                    500,
                )
            except errors.InvalidURI as e:
                return jsonify(erro="Erro! URI invalida!", exception=str(e)), 500
        else:
            return jsonify(erro="Falta argumentos!", argumentos_necessarios=fields), 400
    except TypeError as e:
        return jsonify(erro="Payload JSON nulo ou malformado!", exception=str(e)), 400
