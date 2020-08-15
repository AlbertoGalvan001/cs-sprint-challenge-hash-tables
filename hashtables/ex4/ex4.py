# For an input list of integers, we wish to know which positive numbers
# have corresponding negative numbers in the list.

# Example input:

# ```python
# [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
# ```

# Input can be in any order.

# Example return value:

# ```python
# [ 1, 3, 4 ]
# ```

# Because 1, 3, and 4 are the positive numbers that have corresponding
# negative numbers in the list.

# Return value can be in any order.

# Solve this problem with a hash table.

# Limits:

# * The input list can contain approximately 5,000,000 elements.

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}

    for num in a:
        cache[num] = 1

    for num in a:
        if (num*-1) in cache and num > 0:
            result.append(num)    
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
