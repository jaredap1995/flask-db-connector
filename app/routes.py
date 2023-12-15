from flask import jsonify, request
from app import app, db
from app.models import Users


@app.route("/user", methods=['POST'])
def add_user():
    data = request.json
    new_user = Users(
        first_name = data['firstname'],
        last_name = data['lastname'],
        phone = data['phone'],
        username = data['username'], 
        email = data['email'], 
        password = data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User Added"}), 201

@app.route("/user/<value>", methods = ['GET'])
def get_user(value):
    user = Users.query.filter_by(username = value).first()
    if not user:
        user = Users.query.filter_by(email = value).first()
    if user:
        return jsonify({
            "id": user.id, 
            "username": user.username, 
            "email": user.email,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "phone": user.phone,
            "password": user.password #To be removed
            })
    return jsonify({"message": "User not found"}), 404

@app.route("/user/<user>", methods = ['PUT', 'GET'])
def update_user(user):
    data = request.json
    user = Users.query.get(user)
    print(user)
    if user:
        user.id = user.id
        user.username = data.get('username', user.username)
        user.first_name = data.get('firstname', user.first_name)
        user.last_name = data.get('lastname', user.last_name)
        user.phone = data.get('phone', user.phone)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify({ "message": "User updated"}), 200
    else:
        return jsonify({ "message": "User not found"}), 404


