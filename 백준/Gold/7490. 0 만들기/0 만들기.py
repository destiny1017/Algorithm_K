from itertools import product

x = int(input())
mod = ['+', '-', ' ']

for i in range(x):
    n = int(input())
    prod = list(product(mod, repeat=n - 1))
    results = []
    for item in prod:
        arr = ['1']
        for j in range(n-1):
            arr.append(item[j])
            arr.append(str(j+2))

        if eval(''.join(arr).replace(' ', '')) == 0:
            results.append(arr)

    results.sort()
    for result in results:
        print(''.join(result))
    print()
