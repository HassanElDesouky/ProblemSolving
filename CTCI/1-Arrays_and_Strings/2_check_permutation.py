def check_permutation_1(str1, str2):
    '''
    complexity: O(sort + n)
    '''
    li1 = list(str1)
    li2 = list(str2)
    li1.sort()
    li2.sort()
    return li1 == li2

def check_permutation(str1, str2):
    '''
    complexity: O(n)
    '''
    di1 = {}
    di2 = {}
    for c in str1:
        if c not in di1:
            di1[c] = 1
        else:
            di1[c] += 1
    for c in str2:
        if c not in di2:
            di2[c] = 1
        else:
            di2[c] += 1
    return di1 == di2

print(check_permutation('acd', 'dabc'))
