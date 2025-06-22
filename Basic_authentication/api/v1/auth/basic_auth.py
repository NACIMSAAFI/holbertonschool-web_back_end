#!/usr/bin/env python3
"""BasicAuth class"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class to handle basic authentication."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header."""
        if not authorization_header or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]
