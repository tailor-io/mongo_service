from flask import Blueprint, jsonify, request
from .db import DB

experience_bp = Blueprint("experience", __name__)


@experience_bp.route("/query")
def query():
    args = request.args
    database = DB()
    result = database.getUserExperience(args["user-id"])

    return jsonify(result)


@experience_bp.route("/create", methods=["POST"])
def create():
    args = request.json
    database = DB()
    result = database.createUserExperience(args)

    return "Success!"
