def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    nums_with_opposite = dict()
    corresponding_pair_absolutes = []

    for num in a:

        '''first add nums to dict . 0 has no opposite'''
        nums_with_opposite[num] = 1

        '''Add absolute value to new arr if opposite exists'''
        if -num in nums_with_opposite and num != 0:
            corresponding_pair_absolutes.append(abs(num))

    return corresponding_pair_absolutes


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))