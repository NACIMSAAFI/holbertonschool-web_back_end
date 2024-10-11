#!/usr/bin/env python3
"""
Filtered logger for user data.
"""
from typing import List
import logging
import re

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Obfuscate specified fields in the log message.

    Args:
        fields: A list of strings representing fields to obfuscate.
        redaction: A string representing the obfuscation value.
        message: The log message containing the fields.
        separator: The character separating the fields in the log message.

    Returns:
        The modified log message with specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(
            rf"{re.escape(field)}=.*?{re.escape(separator)}",
            f"{field}={redaction}{separator}",
            message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """
    Uses 'filter_datum' to redact the PII fields in a record message.
    """

    REDACTION = "***"
    FORMAT = "[USER_DATA] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Returns the formatted log message filtered
        to censor sensitive information.
        """
        formatted_msg: str = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, formatted_msg, self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """
    Returns a configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
