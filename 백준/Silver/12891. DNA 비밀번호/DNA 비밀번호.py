n, m = map(int, input().split())
dna = input() + " "
A, C, G, T = map(int, input().split())
acgt = {'A': dna[0:m-1].count('A'),
        'C': dna[0:m-1].count('C'),
        'G': dna[0:m-1].count('G'),
        'T': dna[0:m-1].count('T')}
result = 0

for i in range(n-m+1):
    acgt[dna[i+m-1]] += 1
    if acgt['A'] >= A and acgt['C'] >= C and acgt['G'] >= G and acgt['T'] >= T:
        result += 1
    acgt[dna[i]] -= 1

print(result)