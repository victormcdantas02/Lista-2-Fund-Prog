qtd_clientes = int(input("Digite quantos clientes foram atendidos: "))
total_alertas = 0

for i in range(1, qtd_clientes + 1):
    print(f"\nCliente {i}")
    premium = input("O cliente é premium (S/N): ") == "S"
    qtd_transacoes = int(input("Digite quantas transações foram feitas: "))
    saldo = 0.0

    for j in range(qtd_transacoes):
        tipo = input("Digite o tipo de transação(D para depósito, S para saque): ")
        if tipo not in ("D", "S"):
            print("Tipo inválido, transação ignorada.")
            continue

        valor = float(input("Digite o valor: R$ "))

        if tipo == "D":
            saldo += valor
        else: 
            if valor > 5000 and not premium:
                print("Transação suspeita")
                total_alertas += 1
            saldo -= valor

    print(f"Saldo final do cliente: R$ {saldo:.2f}")

print(f"\nTotal de alertas emitidos: {total_alertas}")