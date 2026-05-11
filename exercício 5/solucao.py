quantidade = int(input("Coloque a quantidade de números: "))
for _ in range(quantidade):
    numero = int(input("Digite o número que deseja calcular o fatorial: "))
    fatorial = 1
    if numero == 0 or numero == 1:
        print(1)
    else:
        for i in range(1, numero + 1):
            fatorial *= i
        print(f"O fatorial de {i} é {fatorial}")