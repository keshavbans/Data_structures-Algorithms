def anagramSolution(s1, s2):
    alist = [ch for ch in s1]
    blist = [ch for ch in s2]


    for i in alist:
        c = 0
        found = True
        while c < len(blist) and not found:
            if i == blist[c]:
                del blist[c]
                found = True

        if c > len(blist):
            return True


    if blist:
        return False
    else:
        return True


def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

#print(anagramSolution1('abcd','dcba'))


def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = False

    #while pos < len(s1) and matches:
     #   if alist1[pos]==alist2[pos]:
      #      pos = pos + 1
       # else:
        #    matches = False
    if alist1 == alist2:
        matches = True

    return matches

print(anagramSolution2('abcde','edcba'))

