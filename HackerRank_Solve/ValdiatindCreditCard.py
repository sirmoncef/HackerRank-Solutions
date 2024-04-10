import re

def validate_credit_card(card):
    # Check if card starts with 4, 5, or 6 and contains only digits and hyphens
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$', card):
        # Remove hyphens and check for consecutive repeated digits
        card = card.replace('-', '')
        if re.search(r'(\d)\1{3,}', card):
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        card_number = input().strip()
        print(validate_credit_card(card_number))
