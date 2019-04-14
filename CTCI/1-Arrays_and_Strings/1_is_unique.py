def is_unique_1(str1):
    di = set()
    for c in str1:
        di.add(c)
    return len(str1) == len(di)

def is_unique(str1):
    li = list(str1)
    li.sort()
    for i in range(1, len(li)):
        if li[i] == li[i-1]:
            return False
    return True

print(is_unique('hello'))
