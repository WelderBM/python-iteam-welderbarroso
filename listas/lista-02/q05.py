# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: welder barroso de melo
# Data:  29-05-2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def aplicar(lista, funcao):
    resultado = []
    for item in lista:
        resultado.append(funcao(item))
    return resultado

# funcao que eleva ao quadrado
def ao_quadrado(n):
    return n ** 2

# funcao que verifica se é par
def eh_par(n):
    return n % 2 == 0

# testando
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = aplicar(numeros, ao_quadrado)
print(f"numeros ao quadrado: {quadrados}")

pares = aplicar(numeros, eh_par)
print(f"eh par: {pares}")

# tambem da pra usar lambda direto
triplos = aplicar(numeros, lambda x: x * 3)
print(f"triplos: {triplos}")
