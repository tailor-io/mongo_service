from flask import Flask
from modules.user import user_bp
from modules.experience import experience_bp
import modules.db as db

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(experience_bp, url_prefix="/user")
app.register_blueprint(user_bp, url_prefix="/user")


# test to insert data to the data base
@app.route("/test")
def test():
    db.db.collection.insert_one({"name": "John"})
    return "Connected to the data base!"


@app.route("/")
def flask_mongodb_atlas():
    return "flask mongodb atlas!"


if __name__ == "__main__":
    app.run()
