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

def validate_url(url):
	"""
	Validate if the given URL string matches the pattern
	Args:
		url (str): The URL to validate.
	Returns:
		bool: True  if URL matches, False otherwise
	"""
	pattern = r"^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$"
	return bool(re.match(pattern, url))

def validate_phone_number(phone_number):
	"""
	Validate if the given phone number matches pattern
	Args:
		phone_number (str): The phone number to validate.
	Returns:
		bool: True if the phone number matches the pattern.
	"""
	pattern = r"^(\(\d{3}\)\s|\d{3}[-.])?\d{3}[-.]\d{4}$"
	return bool(re.match(pattern, phone_number))

def validate_credit_card_number(cc_number):
	"""
	Validate if the given cc number matches pattern
	Args:
		cc_number (str): The credit card number to validate
	Returns:
		bool: True if the credit card number matches the pattern
	"""
	pattern = pattern = r"^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$"
	return bool(re.match(pattern, cc_number))

def validate_time(time_string):
	"""
	Validate if the given time string matches typical time patterns.
	Args:
		time_string (str): The time string to validate.
	Returns:
		bool: True if the time string matches the pattern
	"""
	pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9]$"
	return bool(re.match(pattern, time_string))

def validate_html_tags(tag):
	"""
	Validate if the given hashtag string matches typical hashtag patterns
	Args:
		hashtah (str): The hashtag to validate
	Returns:
		bool: True if the hashtag matches the pattern
	"""
	pattern = r"^#[A-Za-z0-9_]+$"
	return bool(re.match(pattern, hashtag))

def validate_hashtags(hashtag):
	"""
	Validate if the given hashtag string matches the pattern
	Args:
		hashtag (str): The hashtag to validate
	Returns:
		bool: True if match
	"""
	pattern = r"^#[A-Za-z0-9_]+$"
	return bool(re.match(pattern, hashtag))

def validate_currency_amount(currency):
	"""
	Validate if the given currency string matches patttern
	Args:
		currency (str): The currency string
	Returns:
		bool: True if the currency string matches
	"""
	pattern = r"^\$\d{1,3}(,\d{3})*(\.\d{2})?$"
	return bool(re.match(pattern, currency))
