from flask import Blueprint, jsonify, request
from .db import DB

experience_bp = Blueprint("experience", __name__)


@experience_bp.route("/query")
def query():
    args = request.args
    database = DB()
    result = database.getUserExperience(args["user-id"])
    del result["_id"]

    return jsonify(result)


@experience_bp.route("/create")
def create():
    args = request.args.to_dict()
    database = DB()
    result = database.createUserExperience(args)

    return "Success!"
