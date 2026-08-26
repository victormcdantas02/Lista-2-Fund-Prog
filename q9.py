soma_temperaturas = 0
cont_temperaturas = 0

while True:
    temperatura = float(input("Digite a temperatura do paciente, para encerrar a contagem digite -1: "))
    if temperatura == -1:
        break

    soma_temperaturas += temperatura
    cont_temperaturas += 1

if cont_temperaturas == 0:
    print("Nenhuma temperatura foi informada")
else:
    media = soma_temperaturas / cont_temperaturas
    print(f"Foram registradas {cont_temperaturas} temperaturas.")
    print(f"A média das temperaturas é: {media: .2f}" )
