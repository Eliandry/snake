for a in range(4,500):
    for b in range(4,500):
        if a*a+b*b==(1000-a-b)**2:
            result=(a,b,(1000-a-b), a*b*(1000-a-b))
print(result)