#a=list(input().split())

def first_unique_char(a):
    c = 0
    for i in a:
        if a.count(i)==1:
            c=a.find(i)
        else:
            c=-1
    return c
