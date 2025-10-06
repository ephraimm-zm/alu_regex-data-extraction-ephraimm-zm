# ALU Regex Data Extraction - ephraimm-zm

## Project Overview
This project aims to demonstrate the use of Regular Expressions in Python. Below is what we will be extracting using Regular Expression

- Email addresses  
- URLs  
- Phone numbers  
- Credit card numbers  
- Currency amounts  

The project uses Pythons built in regular expression module called re. This module gives access to functions and classes for working with text patterns

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
