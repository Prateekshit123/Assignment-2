tup = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def sort_tuple(tup):
    list = len(tup)
    for i in range(0, list):
        for j in range(0, list-i-1):
            if (tup[j][-1] > tup[j+1][-1]):
                tem_tup = tup[j]
                tup[j] = tup[j+1]
                tup[j+1] = tem_tup
    return tup
print("list of tuple before sorting : ", tup)
print("list of tuple after sorting : ", sort_tuple(tup))