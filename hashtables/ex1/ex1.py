def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    '''impliment new dict'''
    get_weights =  dict()

    for weight_idx in range(len(weights)):

        current_weight = weights[weight_idx]

        # if key is found get index prev weight
        if current_weight in get_weights:

            prev_weight_idx = get_weights[current_weight]

            # rtn cur weight idx in tuple
            return (weight_idx, prev_weight_idx)

        get_weights[limit - current_weight] = weight_idx

    return None
