#!/usr/bin/env python3
""" Auth Class """

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to handle authentication and authorization."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if authentication is needed for a given path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header from the request."""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Returns the current user based on the request."""
        return None
