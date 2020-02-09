def qw(array):
    if len(array)<2:
        return array
    else:
        sredne=array[0]
        less=[i for i in array[1:] if i<=sredne]
        greater=[i for i in array[1:] if i>sredne]
        return qw(less)+[sredne]+qw(greater)
print(qw([10,5,2,3]))