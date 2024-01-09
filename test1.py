# Using the walrus operator, introduced in Python 3.8. Test Test

def check_length(input_list):
    if (n := len(input_list)) > 5:
        return f"List is long (length {n})"
    else:
        return f"List is short (length {n})"

# Example usage
result = check_length([1, 2, 3, 4, 5, 6])
print(result)
