from flask import Blueprint, jsonify, request
from .db import DB

user_bp = Blueprint("user", __name__)


@user_bp.route("/query")
def query():
    args = request.args.to_dict()
    database = DB()
    result = database.getUserInfo(args["user-id"])
    del result["_id"]

    return jsonify(result)


@user_bp.route("/create")
def create():
    args = request.args.to_dict()
    database = DB()
    result = database.createUserInfo(args)

    return "Success!"
