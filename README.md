# ALU Regex Data Extraction - ephraimm-zm

## Project Overview
This project demonstrates the use of **Regular Expressions (Regex)** in Python to extract structured data from unstructured text.

- Email addresses  
- URLs  
- Phone numbers  
- Credit card numbers  
- Currency amounts  

The project is designed as part of the **ALU Regex Data Extraction Assignment** in the Software Engineering program at ALU. The regex patterns handle common edge cases, such as emails with subdomains, URLs with query strings, phone numbers with country codes, credit card numbers in multiple formats, and currency amounts with commas, decimals, and negatives.

---

## Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/ephraimm-zm/alu_regex-data-extraction-ephraimm-zm.git
cd alu_regex-data-extraction-ephraimm-zm
```

2. **Run the Python script**:
```bash
python solution.py
```

3. **Expected Output**:

```
Emails: ['support@example.com', 'john.doe+test@company.co.uk']
URLs: ['https://www.example.com', 'https://sub.example.org/page?ref=home#section']
Phones: ['(123) 456-7890', '123-456-7890', '+1 123 456 7890', '123.456.7890']
Credit Cards: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Currency: ['$19.99', '$1,234.56', '$-500.00']
```
