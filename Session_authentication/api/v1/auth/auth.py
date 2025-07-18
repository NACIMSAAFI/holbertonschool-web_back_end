#!/usr/bin/env python3
"""Auth Class"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class to handle authentication and authorization."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if authentication is needed for a given path."""
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if not path.endswith("/"):
            path += "/"

        for excluded_path in excluded_paths:
            if excluded_path == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header from the request."""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Returns the current user based on the request."""
        return None

    def session_cookie(self, request=None):
        """Returns the session cookie from the request."""
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        my_session_id = request.cookies.get(session_name)
        return my_session_id if my_session_id else None
