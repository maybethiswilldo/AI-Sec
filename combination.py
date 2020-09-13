def combination(lst, r):
    l1 = []
    for elem in lst:
        if elem not in l1:
            l1.append(elem)
    l1.sort()

    def operate(subject, r1):
        res = []
        if r1 > len(subject):
            return "'r' cannot be larger than 'n'"

        if r1 < 1:
            return "'r' has to be larger than 0"
        elif r1 == 1:
            for ele in subject:
                res.append([ele])
        else:
            for i in range(len(subject) - r1 + 1):
                tmp = operate(subject[i+1:], r1 - 1)
                for t in tmp:
                    res.append([subject[i]] + t)

        return res

    result = operate(l1, r)
    return result
