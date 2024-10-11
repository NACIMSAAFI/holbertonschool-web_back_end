#!/usr/bin/env python3
"""
Function called filter_datum that

returns the log message obfuscated.
"""
from typing import List
import re
import logging


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
            f"{field}=.*?{separator}",
            f"{field}={redaction}{separator}",
            message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """
    Uses 'filter_datum' to redact the PII fields
    in a record message.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Returns the 'record.getMessage()',
        formatted using '% self.FORMAT',
        and filtered to censor the sensitive user information,
        using the 'filter_datum' function,
        """
        FORMATTED_MSG: str = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, FORMATTED_MSG, self.SEPARATOR
        )
