from flask import jsonify, request
from app import app, db
from app.models import Users


@app.route("/user", methods=['POST'])
def add_user():
    data = request.json
    new_user = Users(
    #   sql_column_name = data['ObjectState Key Name']
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
            "username": user.username, 
            "email": user.email,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "phone": user.phone,
            "password": user.password #To be removed
            })
    return jsonify({"message": "User not found"}), 404

@app.route("/user/<int:user_id>", methods = ['PUT'])
def update_user(user_id):
    data = request.json()
    user = Users.query.get(user_id)
    if user:
        user.username = data.get('username', user.username)
        user.first_name = data.get('firstname', user.firstname)
        user.last_name = data.get('firstname', user.lastname)
        user.phone = data.get('phone', user.phone)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify({ "message": "User updated"}), 200
    else:
        return jsonify({ "message": "User not found"}), 404


