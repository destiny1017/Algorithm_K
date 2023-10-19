n = int(input())

if n == 1 or n == 3:

    print(-1)

else:

    result = n // 5

    val = n % 5

    if val == 1 or val == 3:

        val += 5

        result -= 1

    

    print(result + (val // 2))

    

    