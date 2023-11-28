from flask import jsonify, request
from app import app, db
from app.models import Users


@app.route("/user", methods=['POST'])
def add_user():
    data = request.json
    new_user = Users(username = data['username'], email = data['email'], password = data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User Added"}), 201

@app.route("/user/<username>", methods = ['GET'])
def get_user(username):
    user = Users.query.filter_by(username = username).first()
    if user:
        return jsonify({"username": user.username, "email": user.email})
    return jsonify({"message": "User not found"}), 404

@app.route("/user/<username>", methods = ['PUT'])
def update_user(username):
    data = request.json()
    user = Users.query.filter_by(username=username).first()
    if user:
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify({ "message": "User updated"}), 200
    else:
        return jsonify({ "message": "User not found"}), 404


