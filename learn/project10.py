all_numbers=[]
for i in range(1,2000000):
    prime=True
    for x in range(2,i):
        if i%x==0:
            prime=False
            break
    if prime:
        all_numbers.append(i)
result=sum(all_numbers)
print(result)
