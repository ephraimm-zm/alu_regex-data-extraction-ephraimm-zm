import re

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s?#]*)?(?:\?[^\s#]*)?(?:#[^\s]*)?'

phone_pattern = r'(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'

credit_card_pattern = r'\b(?:\d[ -]*?){13,16}\b'

currency_pattern = r'\$-?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

def extract_data(pattern, text):
    return re.findall(pattern, text)

sample_text = """
Contact: support@example.com, john.doe+test@company.co.uk
Website: https://www.example.com, https://sub.example.org/page?ref=home#section
Phones: (123) 456-7890, 123-456-7890, +1 123 456 7890, 123.456.7890
Credit cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Currency: $19.99, $1,234.56, $-500.00
"""

print("Emails:", extract_data(email_pattern, sample_text))
print("URLs:", extract_data(url_pattern, sample_text))
print("Phones:", extract_data(phone_pattern, sample_text))
print("Credit Cards:", extract_data(credit_card_pattern, sample_text))
print("Currency:", extract_data(currency_pattern, sample_text))
