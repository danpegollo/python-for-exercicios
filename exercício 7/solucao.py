n = int(input("Digite o valor de N: "))
s = 0
for i in range(1, n + 1):
    s = s + (i / (n - i + 1))
print(f"O valor de S é: {s:.2f}")