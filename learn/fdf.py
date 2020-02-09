numbers =[1,4,3,2,7,9]
n= 1
while n < len(numbers):
    for i in range(len(numbers)-n):
        if numbers[i ]>numbers[i+1]:
            numbers[i] =numbers[i+1]
            numbers[i + 1]=numbers[i+1]
    n+=1
print(numbers)