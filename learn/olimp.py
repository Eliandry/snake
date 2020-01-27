numbers =[52518, 718438, 358883, 462189, 853171, 592966, 225788, 46977, 814826, 295697, 676256, 561479, 56545 , 764281]
maxs = (max(numbers))
print(maxs)
lens = (len(numbers))
credit = []
for i in range(lens):
    f = maxs-numbers[i]
    credit.append(f)

print(credit)
print(sum(numbers))