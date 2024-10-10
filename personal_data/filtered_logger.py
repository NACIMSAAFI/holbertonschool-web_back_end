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


if __name__ == '__main__':
    main()
