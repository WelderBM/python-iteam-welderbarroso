# Lista 02 — Questão 06: Módulo de Estatísticas (programa principal)
# Aluno: welder barroso de melo
# Data:  29-05-2026

from q06_estatisticas import media, mediana, moda, desvio_padrao

# pede 10 notas pro usuario
notas = []
print("digite 10 notas separadas por espaco")
entrada = input("")
partes = entrada.split()

for parte in partes:
    notas.append(float(parte))

# se o usuario nao digitou 10 avisa mas continua
if len(notas) != 10:
    print(f"voce digitou {len(notas)} notas em vez de 10 mas tudo bem vou calcular assim mesmo")

# calcula e exibe
print(f"\nmedia: {media(notas):.2f}")
print(f"mediana: {mediana(notas):.2f}")
print(f"moda: {moda(notas)}")
print(f"desvio padrao: {desvio_padrao(notas):.2f}")
