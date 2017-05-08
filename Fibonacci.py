fibonacci = [1,2]
x = fibonacci[-1]
even = []

while fibonacci[-1] + fibonacci[-2] < 4000000:

    x = fibonacci[-1] + fibonacci[-2]

    fibonacci.append(x)


for x in fibonacci:
    if x % 2 == 0:
        even.append(x)

print(sum(even))
