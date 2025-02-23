#!/usr/bin/env python3

import re

"""
Module for validating various strings using regular expressions.
"""

import re

def validate_email(email):
	"""
	Validate if the given email string matches the pattern for email addresses
	Args:
		email (str): The email address to validate.
	Returns:
		bool: True if the email matches the pattern, False otherwise.
	"""
	pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
	return bool(re.match(pattern, email))
