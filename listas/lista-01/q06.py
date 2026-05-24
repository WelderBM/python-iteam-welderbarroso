# Lista 01 — Questão 06: Validador de Senha
# Aluno: Welder Barroso de Melo
# Data:  24-05-2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────

tentativas = 0
while True:
    print("digite a sua senha ")
    senha = input()
    tentativas += 1
    erros = []
    
    if len(senha) < 8:
        erros.append("precisa ter no minimo 8 caracteres")
        
    tem_digito = False
    for c in senha:
        if c.isdigit():
            tem_digito = True
            break
    if not tem_digito:
        erros.append("precisa ter pelo menos um numero")
        
    tem_maior = False
    for c in senha:
        if c.isupper():
            tem_maior = True
            break
    if not tem_maior:
        erros.append("precisa ter pelo menos uma letra maiuscula")
        
    if not erros:
        print(f"Senha válida após {tentativas} tentativa(s).")
        break
    else:
        print("senha invalida por causa disso aqui")
        for e in erros:
            print(f"- {e}")

