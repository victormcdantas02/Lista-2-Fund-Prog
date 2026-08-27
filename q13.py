acessos_liberados = 0

for i in range(12):
    associacao = input ("É associado da academia? \nDigite S para sim e N para não: ")
    idade = int (input("Digite sua idade: "))

    if associacao == "S" and idade >= 18:
        acessos_liberados += 1

print(f"A quantidade com acesso para a piscina é: {acessos_liberados}")