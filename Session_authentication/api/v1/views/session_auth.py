#!/usr/bin/env python3
"""Session Authentication View"""
from flask import request, jsonify
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def session_login():
    """POST /auth_session/login
    Returns user data after successful login and creates session cookie
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # Step 1: Check email presence
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Step 2: Check password presence
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Step 3: Look up user by email
    users = User.search({"email": email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Step 4: Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Step 5: Create session
    from api.v1.app import auth

    session_id = auth.create_session(user.id)

    # Step 6: Set cookie and return user
    response = jsonify(user.to_json())
    response.set_cookie(getenv("SESSION_NAME"), session_id)
    return response


@app_views.route(
    "/auth_session/logout", methods=["DELETE"], strict_slashes=False)
def session_logout():
    """DELETE /auth_session/logout
    Logs out the user by destroying the session cookie
    """
    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
