import re

def validate_contact_number(number):
    pattern = (
        r"^(?:\+\d{1,3}[ .-]?)?"  # Country code
        r"(?:\(?(\d{3})\)?[ .-]?)"  # Area code
        r"\d{3}[ .-]?"  # Three digits
        r"\d{4}$"  # Four digits
    )

    if re.match(pattern, number):
        return True
    else:
        return False

# Test cases
contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for number in contact_numbers:
    if validate_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
