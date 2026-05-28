# Desafio 08 — Banco Digital
# Aluno: (welder barroso de melo)
# Data:  (28-05-2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

class ContaBancaria:
    # classe que representa uma conta no banco
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        # deposita valor na conta, rejeita se for zero ou negativo
        if valor <= 0:
            print("valor invalido pra deposito, tem que ser maior que zero")
            return
        self.saldo += valor
        print(f"deposito de R${valor:.2f} realizado com sucesso")

    def sacar(self, valor):
        # saca valor da conta, rejeita se nao tiver saldo ou valor invalido
        if valor <= 0:
            print("valor invalido pra saque, tem que ser maior que zero")
            return
        if valor > self.saldo:
            print(f"saldo insuficiente! voce tem R${self.saldo:.2f} e tentou sacar R${valor:.2f}")
            return
        self.saldo -= valor
        print(f"saque de R${valor:.2f} realizado com sucesso")

    def exibir_extrato(self):
        # mostra o titular e o saldo atual
        print(f"\n--- extrato ---")
        print(f"titular: {self.titular}")
        print(f"saldo: R${self.saldo:.2f}")
        print(f"---------------")


# programa principal
conta1 = ContaBancaria("welder barroso")
conta2 = ContaBancaria("joao silva", 100.0)

print("=== conta do welder ===")
conta1.depositar(500)
conta1.depositar(250.50)
conta1.sacar(100)
conta1.exibir_extrato()

print("\n=== conta do joao ===")
conta2.depositar(200)
conta2.sacar(50)
conta2.exibir_extrato()

# testando rejeicao de saque invalido
print("\n=== testando saques invalidos ===")
conta1.sacar(9999)      # saldo insuficiente
conta2.sacar(-10)        # valor negativo
conta2.depositar(0)      # deposito de zero
