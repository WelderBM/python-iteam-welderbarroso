# Desafio 03 — Sistema de Multas
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
print("Qual é a velocidade do seu carro em km/h?")
velocidade = float(input(""))

if velocidade > 80 :
    excedente = velocidade - 80
    multa = excedente * 7
    print(f"Multado! Você excedeu o limite de 80km/h. Sua multa será de {multa} sete reais")
else:
    print("Boa viagem! Dirija com segurança")