qtd_veiculos = int(input("Digite a quantidade de veículos: "))
total_sinalizados = 0

for i in range(1, qtd_veiculos + 1):
    print(f"\nVeículo {i}")
    
    while True:
        tipo_veiculo = input("Tipo do veículo (diesel/gasolina): ")
        if tipo_veiculo in ("diesel", "gasolina"):
            break
        print("Tipo inválido. Digite 'diesel' ou 'gasolina'.")

    while True:
        qtd_dias = int(input("Quantos dias abasteceu (1 a 7): "))
        if 1 <= qtd_dias <= 7:
            break
        print("Número deve estar entre 1 e 7.")
    
    total_litros = 0.0

    for dia in range(1, qtd_dias + 1):
        print(f"  Dia {dia}:")
        tipo_comb = input("  Combustível usado (gasolina/diesel): ")
        
        if tipo_comb not in ("gasolina", "diesel"):
            print(" Tipo de combustível inválido. Abastecimento ignorado.")
            continue
        
        litros = float(input("Digite quantos litros foram colocados no tanque: "))
        total_litros += litros
    
    if tipo_veiculo == "diesel" and total_litros > 300:
        print("Consumo acima do esperado")
        total_sinalizados += 1
    
    print(f"Total de litros do veículo {i}: {total_litros:.2f}")

print(f"\nTotal de veículos sinalizados: {total_sinalizados}")