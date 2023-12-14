# Using the walrus operator, introduced in Python 3.8. 

def check_length(input_list):
    if (len(input_list)) > 5:
        return f"List is long"
    else:
        return f"List is short"

# Example usage
result = check_length([1, 2, 3, 4, 5, 6])
print(result)
