import unittest
import re
from regex_extractor import email_pattern, url_pattern, phone_pattern, credit_card_pattern, currency_pattern, extract_data

class TestRegexExtraction(unittest.TestCase):
    def setUp(self):
        self.sample_text = """
        Contact: support@example.com, john.doe+test@company.co.uk
        Website: https://www.example.com, https://sub.example.org/page?ref=home#section
        Phones: (123) 456-7890, 123-456-7890, +1 123 456 7890, 123.456.7890
        Credit cards: 1234 5678 9012 3456, 1234-5678-9012-3456
        Currency: $19.99, $1,234.56, $-500.00
        """

    def test_emails(self):
        expected = ['support@example.com', 'john.doe+test@company.co.uk']
        result = extract_data(email_pattern, self.sample_text)
        self.assertEqual(result, expected)

    def test_urls(self):
        expected = ['https://www.example.com', 'https://sub.example.org/page?ref=home#section']
        result = extract_data(url_pattern, self.sample_text)
        self.assertEqual(result, expected)

    def test_phones(self):
        expected = ['(123) 456-7890', '123-456-7890', '+1 123 456 7890', '123.456.7890']
        result = extract_data(phone_pattern, self.sample_text)
        self.assertEqual(result, expected)

    def test_credit_cards(self):
        expected = ['1234 5678 9012 3456', '1234-5678-9012-3456']
        result = extract_data(credit_card_pattern, self.sample_text)
        self.assertEqual(result, expected)

    def test_currency(self):
        expected = ['$19.99', '$1,234.56', '$-500.00']
        result = extract_data(currency_pattern, self.sample_text)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
