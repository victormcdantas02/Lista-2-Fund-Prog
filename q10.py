total = 0
quantidade = 0

while True:
    valor = float(input("Digite o valor da venda: "))

    if valor < 0:
        print("Valor inválido")
        continue
    elif valor == 0:
        break

    total += valor
    quantidade += 1

print(f"O valor total da venda é: R$ {total:.2f}")
print(f"A quantidade de vendas foi de {quantidade}")