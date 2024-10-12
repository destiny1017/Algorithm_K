n, m = map(int, input().split())
pays = [int(pay) for pay in input().split()]
prev_pay = sum(pays[0:m])
max_pay = prev_pay

for i in range(m, n):
    prev_pay = prev_pay - pays[i-m] + pays[i]
    max_pay = max(max_pay, prev_pay)

print(max_pay)