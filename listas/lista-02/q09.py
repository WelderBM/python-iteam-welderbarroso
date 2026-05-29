# Lista 02 — Questão 09: Encapsulamento e Propriedades
# Aluno: welder barroso de melo
# Data:  29-05-2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py — classe Produto com:
#   1. __preco via @property com validação (preço > 0)
#   2. __estoque com getter, repor(qtd) e vender(qtd) — ValueError se sem estoque
#   3. __str__ informativo e __repr__ para debug
# Demonstre: criação, vendas, reposição e tentativa de venda além do estoque.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.__preco = 0
        self.__estoque = 0
        # usa o setter pra validar
        self.preco = preco
        self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("preco tem que ser maior que zero")
        self.__preco = valor

    @property
    def estoque(self):
        return self.__estoque

    def repor(self, qtd):
        if qtd <= 0:
            print("quantidade tem que ser positiva")
            return
        self.__estoque += qtd
        print(f"reposto {qtd} unidades de {self.nome}. estoque atual: {self.__estoque}")

    def vender(self, qtd):
        if qtd <= 0:
            raise ValueError("quantidade tem que ser positiva")
        if qtd > self.__estoque:
            raise ValueError(f"estoque insuficiente. tem so {self.__estoque} unidades de {self.nome}")
        self.__estoque -= qtd
        print(f"vendido {qtd} unidades de {self.nome}. estoque atual: {self.__estoque}")

    def __str__(self):
        return f"{self.nome} | Preço: R$ {self.__preco:.2f} | Estoque: {self.__estoque}"

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preco={self.__preco}, estoque={self.__estoque})"


# demonstracao
p1 = Produto("Caneta Azul", 2.50, 100)
p2 = Produto("Caderno 200fls", 25.00, 30)

print(p1)
print(p2)

# vendendo
p1.vender(10)
p2.vender(5)

# repondo
p1.repor(50)

print(f"\ndepois das operacoes:")
print(p1)
print(p2)

# tentando vender mais do que tem
print("\ntentando vender 100 cadernos com so 25 em estoque:")
try:
    p2.vender(100)
except ValueError as e:
    print(f"erro: {e}")

# tentando preco negativo
print("\ntentando criar produto com preco negativo:")
try:
    p3 = Produto("Teste", -5, 10)
except ValueError as e:
    print(f"erro: {e}")

# mostrando o repr pra debug
print(f"\nrepr: {repr(p1)}")
