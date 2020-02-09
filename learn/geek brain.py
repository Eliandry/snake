def error(numbers):

    if numbers==13:
        raise ValueError()
    else:
        return numbers **2
i=int(input())
try:
    result=error(i)
except ValueError:
    print('несчастливое число')
else:
    print(result)

