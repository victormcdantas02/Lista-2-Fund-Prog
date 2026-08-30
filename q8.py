total_clientes = 1

for i in range(8):
    compra_cliente = float(input("Digite o valor total da compra: "))
    if compra_cliente > 50:
            total_clientes += 1

print (f"Compras que ultrapassaram o valor: {total_clientes}")
