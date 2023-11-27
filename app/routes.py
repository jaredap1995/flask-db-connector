from flask import jsonify, request
from app import app, db
from app.models import Users


@app.route("/user", methods=['POST'])
def add_user():
    data = request.json
    new_user = Users(username = data['username'], email = data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User Added"}), 201

@app.route("/user/<username>", methods = ['GET'])
def get_user(username):
    user = Users.query.filter_by(username = username).first()
    if user:
        return jsonify({"username": user.username, "email": user.email})
    return jsonify({"message": "User not found"}), 404

