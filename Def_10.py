def only_one_positive(*args):
    count=0
    for i in args:
        if i >0:
            count+=1
    if count==0:
        return False
    elif count==1:
        return True
    else:
        return False
