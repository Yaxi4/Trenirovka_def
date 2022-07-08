#a=list(input().split())

def find_duplicate(a):
    c = []
    for i in a:
        if i not in c and a.count(i)>1:
            c.append(i)
    return c
find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2])