def fatorial(num):
    fatorial = 1
    if num == 0 or num == 1:
        return 1
    else:
        for n in range(1, num + 1):
            fatorial *= n
    return fatorial
num = int(input("Coloque um número inteiro e natural: "))
print(fatorial(num))
