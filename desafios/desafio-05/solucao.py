# Desafio 05 — Gerenciador de Compras
# Aluno: (welder barroso de melo)
# Data:  (24-05-2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

produtos = []

stop = False
while not stop:
    print("Digite o nome do produto (ou 'fim' para encerrar): ")
    novo_produto = input()
    if novo_produto == 'fim':
        stop = True
    else:
        produtos.append(novo_produto)

print("Lista de produtos:")
for produto in produtos:
    print(f"- {produto}")
# tamanho da lista
print(f"Total de produtos: {len(produtos)}")