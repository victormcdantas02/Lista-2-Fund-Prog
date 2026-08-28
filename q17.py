qtd_participantes = int(input("Quantos participantes? "))

desempenho_ouro = 0
desempenho_prata = 0
desempenho_bronze = 0

for i in range(1, qtd_participantes + 1):
    print(f"\nParticipante {i}")
    tempo_total = 0
    for j in range(1, 4):
        tempo = float(input(f"Tempo da etapa {j} (minutos): "))
        tempo_total += tempo

    if tempo_total <= 30:
        class_desempenho = "Ouro"
        desempenho_ouro += 1          
    elif tempo_total <= 45:
        class_desempenho = "Prata"
        desempenho_prata += 1
    else:
        class_desempenho = "Bronze"
        desempenho_bronze += 1

print(f"\nTempo total dos participantes: {tempo_total:.2f} minutos e Classificação {class_desempenho}")

print("\nResumo das classificações")
print(f"Ouro: {desempenho_ouro} participante(s)")
print(f"Prata: {desempenho_prata} participante(s)")
print(f"Bronze: {desempenho_bronze} participante(s)")