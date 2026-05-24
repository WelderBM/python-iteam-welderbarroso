# Lista 01 — Questão 07: Progressão e Análise
# Aluno: Welder Barroso de Melo
# Data:  24-05-2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

notas = []

# usei o for aqui porque a gente sabe que sao exatamente 10 notas para ler
for i in range(10):
    # usei o while porque nao sabemos quantas vezes o usuario vai errar ate digitar certo
    while True:
        try:
            print(f"digite a nota {i + 1} de zero a dez ")
            nota = float(input())
            if 0.0 <= nota <= 10.0:
                notas.append(nota)
                break
            else:
                print("tem que ser de zero a dez tenta de novo")
        except ValueError:
            print("digite um numero valido")

maior = max(notas)
menor = min(notas)
media = sum(notas) / 10

acima = 0
# usei o for pra passar em cada nota da lista e ver quem passou da media
for n in notas:
    if n > media:
        acima += 1

if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média: {media:.2f}")
print(f"Quantidade acima da média: {acima}")
print(f"Classificação: {situacao}")

