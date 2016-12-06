def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    work_L = L
    max_value = 0
    current_value = 0
    max_current_combo = []
    current_combo = []
    while len(work_L) > 0:
        for i in range(len(work_L)):
            current_combo.append(work_L[i])
            current_value += work_L[i]
            if current_value > max_value:
                max_value = current_value
                max_current_combo = current_combo[:]
        del current_combo[:]
        current_value = 0
        del work_L[0]

    print(max_current_combo)
    return max_value


my_list = [4, 5, -3, 2, -1]

print(max_contig_sum(my_list))
