result=[]
for i in range(1,500000):
    prime=True
    for x in range(2, i):
        if i%x ==0:
            prime=False
            break
    if prime:
        result.append(i)
    if len(result)==10002:
        break
print(result[10001])
