import re

def is_valid_UID(uid):
    if len(uid) != 10:
        return False
    if len(set(uid)) != len(uid):
        return False
    if not re.match(r'^[A-Za-z0-9]{10}$', uid):
        return False
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    if len(re.findall(r'[0-9]', uid)) < 3:
        return False
    return True

def validate_UIDs(test_cases):
    for case in test_cases:
        if is_valid_UID(case):
            print("Valid")
        else:
            print("Invalid")

if __name__ == "__main__":
    num_test_cases = int(input())
    test_cases = [input().strip() for _ in range(num_test_cases)]
    validate_UIDs(test_cases)
