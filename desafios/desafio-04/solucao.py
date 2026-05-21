# Desafio 04 — Tabuada Personalizada
# Aluno: (welder barroso de melo)
# Data:  (21-05-2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
print("me diga um número de 1 a 10 que te direi a tabuada dele")
input_numero = -1
count = 0
while ( count == 0):
    try:        
        input_numero = int(input())
        if (input_numero < 0 or input_numero > 10):
            raise ValueError("o número deve ser entre 1 e 10")
        elif(input_numero != 0):
                num = 1
                while (num <= 10):
                    print(f"{num} * {input_numero} é igual a {num * input_numero}")
                    num+=1
                print("digite mais um número ou digite 0 para sair.")
        else:
            count+= 1
    except ValueError:
        print("deve ser um número inteiro entre 1 e 10. Tente novamente. Digite 0 para sair")
print("programa finalizado")