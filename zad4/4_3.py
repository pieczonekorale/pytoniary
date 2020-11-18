def sum_calc(L):
    result = []
    for x in L:
        temp = 0
        #  if isinstance(x, list):
       # print(x)
        if len(x)==0:
            result.append(0)
        else:
            for i in x:
                temp = temp + i
            result.append(temp)
    return result


example = [[],[4],(1,2),[3,4],[3,4,5],(5,6,7), (6, 8, 77, 88), (19, 7, 8), [9999, 1]]
print(example)
print(sum_calc(example))