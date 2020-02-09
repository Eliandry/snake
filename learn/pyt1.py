def binary_search(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)
        guesss=list[mid]
        if guesss==item:
            return mid
        if guesss>item:
            high=mid-1
        else:
            low=mid+1

