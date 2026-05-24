# Desafio 02 — Calculadora de IMC
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

nome = input("Qual é o seu nome? ")
peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é sua altura? "))
imc = peso / (altura ** 2)
print(f"Olá {nome}, seu IMC é {imc:.2f}")
