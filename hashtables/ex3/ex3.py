def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    '''How otften does each number show up ?'''
    num_instance = dict()

    for array in arrays:

        for num in array:

            if num in num_instance:
                num_instance[num] += 1
            else:
                num_instance[num] = 1
    
    '''Return numbers that show up for as many times as there are arrays'''
    return [result[0] for result in num_instance.items() if result[1] == len(arrays)]

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
