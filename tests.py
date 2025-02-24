#!/usr/bin/python3
"""
Test module for validating various strings using regex_validations.py.
"""

import unittest
from solution import (
    validate_email,
    validate_url,
    validate_phone_number,
    validate_credit_card_number,
    validate_time,
    validate_html_tags,
    validate_hashtags,
    validate_currency_amount
)

class TestRegexValidations(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(validate_email("user@example.com"))
        self.assertTrue(validate_email("firstname.lastname@company.co.uk"))
        self.assertFalse(validate_email("user@.com"))
        self.assertFalse(validate_email("user@com"))

    def test_validate_url(self):
        self.assertTrue(validate_url("https://www.example.com"))
        self.assertTrue(validate_url("https://subdomain.example.org/page"))
        self.assertFalse(validate_url("http:/example.com"))
        self.assertFalse(validate_url("www.example.com"))

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("(123) 456-7890"))
        self.assertTrue(validate_phone_number("123-456-7890"))
        self.assertTrue(validate_phone_number("123.456.7890"))
        self.assertFalse(validate_phone_number("1234567890"))
        self.assertFalse(validate_phone_number("123-45-7890"))

    def test_validate_credit_card_number(self):
        self.assertTrue(validate_credit_card_number("1234 5678 9012 3456"))
        self.assertTrue(validate_credit_card_number("1234-5678-9012-3456"))
        self.assertFalse(validate_credit_card_number("1234567890123456"))
        self.assertFalse(validate_credit_card_number("1234 5678 9012 345"))

    def test_validate_time(self):
        self.assertTrue(validate_time("14:30"))
        self.assertTrue(validate_time("2:30"))
        self.assertFalse(validate_time("24:00"))
        self.assertFalse(validate_time("14:60"))

    def test_validate_html_tags(self):
        self.assertTrue(validate_html_tags("<p>"))
        self.assertTrue(validate_html_tags('<div class="example">'))
        self.assertTrue(validate_html_tags('<img src="image.jpg" alt="description" />'))
        self.assertFalse(validate_html_tags("<div>"))
        self.assertFalse(validate_html_tags("<img>"))

    def test_validate_hashtags(self):
        self.assertTrue(validate_hashtags("#example"))
        self.assertTrue(validate_hashtags("#ThisIsAHashtag"))
        self.assertFalse(validate_hashtags("example"))
        self.assertFalse(validate_hashtags("#123"))

    def test_validate_currency_amount(self):
        self.assertTrue(validate_currency_amount("$19.99"))
        self.assertTrue(validate_currency_amount("$1,234.56"))
        self.assertFalse(validate_currency_amount("19.99"))
        self.assertFalse(validate_currency_amount("$1234.56"))

if __name__ == "__main__":
    unittest.main()
