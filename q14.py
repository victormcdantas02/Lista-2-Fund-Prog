meia_entrada = 0
inteira = 0

for i in range(10):
    estudante = input ("Você é estudante? \nDigite S para sim e N para não: ")
    idade = int (input("Digite sua idade: "))

    if estudante == "S" or idade >= 60:
        meia_entrada += 1
    else:
        inteira += 1

print(f"A quantidade de ingressos de meia-entrada vendidos é: {meia_entrada}")
print(f"A quantidade com ingressos inteiros vendidos é: {inteira}")