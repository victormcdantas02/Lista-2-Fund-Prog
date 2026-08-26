distancia_incial = int(input("Digite a distância inicial em km: "))
distancia_final = int(input("Digite a distância final em km: "))
incremento = int(input("Digite o incremento semanal: "))

print("\nA progressão semanal a ser percorrida é: ")
for i in range(distancia_incial, distancia_final + 1, incremento):
    print(f"{i} km")