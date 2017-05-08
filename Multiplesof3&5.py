count = 0

for i in range(1, 1000):
    if i % 3 == 0:
        count += i
    elif i % 5 == 0:
        count += i
    elif i % 3 ==0 and i % 5 == 0:
        count += i;
    else:
        continue

print(count)
