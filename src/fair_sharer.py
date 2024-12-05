def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args
    values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """
    # code
    values_new = []
    for i in range(num_iterations):
        max_value_index = values.index(max(values))
        share_of_value = values[max_value_index] * share

        values[max_value_index] -= share_of_value * 2
        values[max_value_index - 1] += share_of_value
        values[max_value_index + 1] += share_of_value
    values_new = values
    return values_new


if __name__ == "__main__":
    print(fair_sharer([0, 1000, 800, 0], 1))  # --> [100, 800, 900, 0]
    print(fair_sharer([0, 1000, 800, 0], 2))  # --> [100, 890, 720, 90]
