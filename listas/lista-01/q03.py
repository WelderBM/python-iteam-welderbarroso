# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
print("Me diga seu nome:")
nome_completo = input()
print("Me diga seu CPF:")
CPF = input()
print("Me diga sua altura:")
altura = float(input())

idade = 0
while (idade == 0):
    try:        
        print("Me diga sua data de nascimento. ex: 2003")
        ano_nascimento = input()
        
        ano_numero = int(ano_nascimento)
        idade = 2026 - ano_numero
    except ValueError:
        print("ano de nascimento só pode ser número. ex: 2003")
        
print(f"{nome_completo}, CPF ({CPF}, tem {idade} anos e tem {altura} de altura)")

#altura deve ser float porque um número com casas decimais não é inteiro