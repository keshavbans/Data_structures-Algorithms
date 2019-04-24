def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if item == alist[midpoint]:
            found = True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found


def recBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recBinarySearch(alist[:midpoint], item)
            else:
                return recBinarySearch(alist[midpoint+1:], item)


testSample = [1,2,4,5,6,7,8,9,12,147,228,336]
print (recBinarySearch(testSample, 15))
