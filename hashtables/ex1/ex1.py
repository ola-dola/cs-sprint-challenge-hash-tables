def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i, val in enumerate(weights):
        if limit-val in cache:
            return (i, cache[limit-val])
        else:
            cache[val] = i

    return None


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
