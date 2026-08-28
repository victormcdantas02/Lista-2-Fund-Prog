total_fabrica = 0
qtd_turnos = int(input("Quantos turnos foram realizados: "))

for i in range(1, qtd_turnos + 1):
    total_turno = 0
    print(f"\nTurno {i}")

    for j in range(1, 4):
        pecas = int(input(f"Peças produzidas na linha {j}: "))
        total_turno += pecas

    print(f"Total produzido no turno {j}: {total_turno}")
    total_fabrica += total_turno

print(f"\nTotal geral da fábrica: {total_fabrica}")