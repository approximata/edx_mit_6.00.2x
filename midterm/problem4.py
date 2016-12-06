def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    work_L = L[:]
    result = {}
    remainder = s
    # while remainder > 0:

    for value in work_L:
        print(remainder)
        if remainder // value >= 1:
            result[value] = remainder // value
            remainder = remainder - value * result[value]
        # break

    print(result)
    if remainder != 0:
        return "no solution"
    else:
        return sum(result.values())

list1 = [5, 3, 2]
s1 = 12

print(greedySum(list1, s1))
