total_alunos = int(input("Digite a quantidade de alunos na turma:"))
alunos_aprovados = 0

for i in range(1, total_alunos  + 1):
    print(f"\nAluno {i}")
    soma_notas = 0

    for j in range(1, 5):
        nota = float(input(f"Digite a nota {j}: "))
        soma_notas += nota

    media = soma_notas/4
    print(f"Média do aluno {i} é: {media:.2f}")

    if media >= 7.0:
        alunos_aprovados += 1

print(f"\nTotal de alunos aprovados: {alunos_aprovados}")