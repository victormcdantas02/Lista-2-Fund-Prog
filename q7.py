total_aprovados = 1

for i in range(10):
    nota = float(input ("Digite a nota do aluno: "))
    if nota >= 7.0:
       total_aprovados += 1

print(f"Alunos aprovados: {total_aprovados}")