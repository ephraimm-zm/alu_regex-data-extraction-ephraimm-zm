#!/usr/bin/env python3

import re

def validate_email(email):
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def validate_url(url):
    """Validate URL format."""
    pattern = r"^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$"
    return bool(re.match(pattern, url))

def validate_phone_number(phone_number):
    """Validate phone number format."""
    pattern = r"^(\(\d{3}\)\s|\d{3}[-.])?\d{3}[-.]\d{4}$"
    return bool(re.match(pattern, phone_number))

def validate_credit_card_number(cc_number):
    """Validate credit card number format."""
    pattern = r"^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$"
    return bool(re.match(pattern, cc_number))

def validate_time(time_string):
    """Validate time format (HH:MM)."""
    pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9]$"
    return bool(re.match(pattern, time_string))

def validate_hashtags(hashtag):
    """Validate hashtag format."""
    pattern = r"^#[A-Za-z0-9_]+$"
    return bool(re.match(pattern, hashtag))

def validate_currency_amount(currency):
    """Validate currency amount format (e.g., $1,234.56)."""
    pattern = r"^\$\d{1,3}(,\d{3})*(\.\d{2})?$"
    return bool(re.match(pattern, currency))
