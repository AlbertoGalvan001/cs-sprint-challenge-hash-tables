# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`. Your
# function will return a tuple of integers that has the following form:

# ```
# (zero, one)
# ```

# where each element represents the item weights of the two packages.
# _**The higher valued index should be placed in the `zeroth` index and
# the smaller index should be placed in the `first` index.**_ If such a
# pair doesn’t exist for the given inputs, your function should return
# `None`.

# Your solution should run in linear time.

# Example:
# ```
# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
# ```

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}

    for value, key in enumerate(weights):
        if key not in weight_dict:
            weight_dict[key] = [value]
        else:
            weight_dict[key].append(value)   

    for weight in weight_dict:
        if limit - weight in weight_dict:
            if weight_dict[weight][0] > weight_dict[limit - weight][0]:
                return (weight_dict[weight][0], weight_dict[limit - weight][0])
            elif weight == limit - weight:
                return (weight_dict[weight][1], weight_dict[weight][0])
            else:
                return (weight_dict[limit - weight][0], weight_dict[weight][0])                 
    return None
