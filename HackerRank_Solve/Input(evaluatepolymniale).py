x, k = map(int, input().split())
polynomial = input()

# Define a function to evaluate the polynomial expression
def evaluate_polynomial(x, polynomial):
    # Replace 'x' with the value of x and evaluate the expression
    result = eval(polynomial)
    return result

# Check if the evaluated result is equal to k
if evaluate_polynomial(x, polynomial) == k:
    print(True)
else:
    print(False)
