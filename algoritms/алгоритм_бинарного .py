def binary(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)
        guess = list[mid]
        if guess==item:

            return mid
        elif guess > item:
            high =mid-1
        else:
            low = mid +1
    return None
my_list = [1, 3, 5, 7, 9]
f = (binary(my_list,5))
print(my_list[f])