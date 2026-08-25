cont = 1
total = 0

while cont <= 5:
    valor_venda = float(input("Digite o valor da compra: "))
    total = total + valor_venda
    cont += 1

print("O valor total de vendas é: ", total)