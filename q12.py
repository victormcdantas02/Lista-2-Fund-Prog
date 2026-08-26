preco_inicial = int(input("Digite o preço inicial: "))
preco_final = int(input("Digite o preço final desejado: "))
valor_reducao = int(input("Digite o valor de cada redução: "))

print("\nPreços durante a liquidação:")
for preco in range(preco_inicial, preco_final -1, -valor_reducao):
    print(f"Preço após redução: R$ {preco}")