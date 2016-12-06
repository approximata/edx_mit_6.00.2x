def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    work_L = L
    max_value = 0
    current_value = 0

    while len(work_L) > 0:
        for i in range(len(work_L)):
            current_value += work_L[i]
            if current_value > max_value:
                max_value = current_value
        current_value = 0
        del work_L[0]

    return max_value


my_list = [4, 5, -5, 2, 9, -4]

print(max_contig_sum(my_list))
