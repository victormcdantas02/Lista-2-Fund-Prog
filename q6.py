qtd_exercicios = int(input("Digite quantos exercícios foram feitos:"))

cont = 1
total = 0

while cont <= qtd_exercicios:
    calorias = float(input(f"Digite quantas calorias foram gastas no exercício: "))
    total = total + calorias
    cont += 1

print("O total de calorias gastas no treino foi: ", total)