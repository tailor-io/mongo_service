from flask import Blueprint, jsonify, request
from .db import DB

education_bp = Blueprint("education", __name__)


@education_bp.route("/query")
def query():
    args = request.args
    database = DB()
    result = database.getUserEducation(args["user-id"])

    return jsonify(result)


@education_bp.route("/create", methods=["POST"])
def create():
    args = request.json
    database = DB()
    result = database.createUserEducation(args)

    return "Success!"
