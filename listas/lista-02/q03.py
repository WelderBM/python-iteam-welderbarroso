# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: welder barroso de melo
# Data:  29-05-2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario.append(produto)
    print(f"produto {nome} adicionado")

def buscar_por_codigo(inventario, codigo):
    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto
    return None

def listar_abaixo_do_minimo(inventario, minimo):
    abaixo = []
    for produto in inventario:
        if produto["quantidade"] < minimo:
            abaixo.append(produto)
    return abaixo

def valor_total(inventario):
    total = 0
    for produto in inventario:
        total += produto["quantidade"] * produto["preco"]
    return total

# programa principal pra demonstrar
inventario = []

# adicionando 3 produtos
adicionar_produto(inventario, "Caneta", "C001", 50, 2.50)
adicionar_produto(inventario, "Caderno", "C002", 3, 15.00)
adicionar_produto(inventario, "Borracha", "C003", 100, 1.00)

# buscando por codigo
print("\nbuscando produto C002:")
resultado = buscar_por_codigo(inventario, "C002")
if resultado:
    print(f"  encontrado: {resultado['nome']} - qtd: {resultado['quantidade']} - preco: R$ {resultado['preco']:.2f}")
else:
    print("  nao encontrado")

# listando abaixo do minimo
print("\nprodutos com menos de 10 unidades:")
poucos = listar_abaixo_do_minimo(inventario, 10)
for p in poucos:
    print(f"  {p['nome']}: {p['quantidade']} unidades")

# valor total em estoque
print(f"\nvalor total do inventario: R$ {valor_total(inventario):.2f}")
