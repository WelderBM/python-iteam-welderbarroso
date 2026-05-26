# Desafio 06 — Bio-Cadastro
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
print("adicione colaboradores na lista.")
equipe = []
stop = False

while stop == False:
    print('Qual seu nome? Ou digite "sair" para encerrar')
    nome = input("")
    if nome != "sair":
        print("Qual seu cargo?")
        cargo = input("")
        equipe.append({"nome": nome, "cargo": cargo})
    else: 
        stop = True
        
for f in equipe:
    print(f"Funcionário: {f['nome']} | Cargo: {f['cargo']}")
