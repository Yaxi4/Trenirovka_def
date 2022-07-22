def seach(array, elem, start,end):
    mid=(start+end)//2
    if elem==array[mid]:
        return mid
    if elem < array[mid]:
        return seach(array,elem,start,mid-1)
    else:
        return seach(array,elem,mid+1,end)
print(seach([1,2,4,6,7,8],4,0,5))