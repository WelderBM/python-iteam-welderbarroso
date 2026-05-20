# Desafio 03 — Sistema de Multas
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
velocidade = input("Qual é a velocidade do seu carro em km/h?")

if velocidade > 80 :
    print("Multado! Você excedeu o limite de 80km/h")
    excedente = velocidade - 80
    multa = excedente * 7
else:
    print("Boa viagem! Dirija com segurança")