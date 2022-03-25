tup = [(1,3),(4,5),(-2,-3),(2,-1)]

def key_sort(tup):
    return tup[1]
    
print("List of tuple before sorting :", tup)
print("list of tuple after sorting :", sorted(tup, key = key_sort))