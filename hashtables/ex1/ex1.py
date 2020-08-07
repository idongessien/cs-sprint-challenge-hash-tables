def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #new dict
    get_weights =  dict()

    for weight_index in range(len(weights)):

        current_weight = weights[weight_index]

        # if found ...
        if current_weight in get_weights:

            # get prev weight
            prev_weight_index = get_weights[current_weight]

            # return current index tuple
            return (weight_index, prev_weight_index)

        get_weights[limit - current_weight] = weight_index

    return None
