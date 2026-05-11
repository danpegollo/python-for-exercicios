quantidade = int(input("Coloque a quantidade de empregados: "))
for _ in range(quantidade):
    nome = input("Coloque o nome do funcionário: ")
    salario = float(input("Coloque o salário do funcionário: "))
    if salario >= 3000:
        novo_salario = salario + (salario * 0.08)
    elif salario >= 2000:
        novo_salario = salario + (salario * 0.10)
    else:
        novo_salario = salario + (salario * 0.12)
    print(f"O nome do funcionário é: {nome}")
    print(f"O salário do funcionário é: R$ {salario:.2f}")
    print(f"O salário ajustado de {nome} é R$ {novo_salario:.2f}")