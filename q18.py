qtd_caminhoes = int(input("Quantos caminhões na frota? "))

for i in range(1, qtd_caminhoes + 1):
    print(f"\nCaminhões {i}")

    pacote_leve = 0
    pacote_medio = 0
    pacote_pesado = 0

    qtd_pacotes = int(input("Quantos pacotes este caminhão transporta? "))

    for j in range(1, qtd_pacotes + 1):
        peso = float(input(f"Peso do pacote {j} (kg): "))
        if peso <= 5:
            categoria = "Leve"
            pacote_leve += 1
        elif peso <= 20:
            categoria = "Médio"
            pacote_leve += 1
        else:
            categoria = "Pesado"
            pacote_pesado += 1

        print(f"Pacote {j}: {peso} kg. Pacote é {categoria}")
        
    print(f"\nResumo do Caminhão {i}:")
    print(f"  Leves: {pacote_leve}")
    print(f"  Médios: {pacote_medio}")
    print(f"  Pesados: {pacote_pesado}")
