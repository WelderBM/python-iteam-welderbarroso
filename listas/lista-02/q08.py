# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: welder barroso de melo
# Data:  29-05-2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        # gerente ganha 20% de bonus
        return self.salario * 0.20

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def calcular_bonus(self):
        # estagiario ganha 5% de bonus
        return self.salario * 0.05

# cria lista com os 3 tipos
equipe = [
    Funcionario("carlos", 3000),
    Gerente("ana", 8000, "TI"),
    Estagiario("pedro", 1500, "engenharia de software")
]

# percorre a lista e exibe o bonus de cada um
# o python chama a versao correta de calcular_bonus sem precisar verificar
# o tipo do objeto porque ele usa o metodo da classe mais especifica
# isso é polimorfismo - cada objeto sabe qual versao do metodo usar
for pessoa in equipe:
    bonus = pessoa.calcular_bonus()
    print(f"{pessoa.nome}: salario R$ {pessoa.salario:.2f} | bonus R$ {bonus:.2f}")
