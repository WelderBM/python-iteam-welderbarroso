# Desafio 09 — Sistema de Frota
# Aluno: (welder barroso de melo)
# Data:  (28-05-2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

# classe pai com os dados basicos de qualquer veiculo
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__quilometragem = 0.0  # privado, ninguem mexe direto

    def get_km(self):
        return self.__quilometragem

    def rodar(self, km):
        if km < 0:
            print("erro: não da pra rodar km negativo, ignorando...")
        else:
            self.__quilometragem += km
            print(f"rodou {km} km com sucesso")

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Quilometragem: {self.get_km()} km")


# caminhao herda de veiculo e adiciona capacidade de carga
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.capacidade_carga = capacidade_carga  # em toneladas

    def exibir_dados(self):
        print("--- CAMINHÃO ---")
        super().exibir_dados()
        print(f"Capacidade de carga: {self.capacidade_carga} toneladas")


# moto herda de veiculo e adiciona cilindrada
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada  # em cc

    def exibir_dados(self):
        print("--- MOTO ---")
        super().exibir_dados()
        print(f"Cilindrada: {self.cilindrada} cc")


# programa principal
print("=== SISTEMA DE FROTA ===\n")

# criando um caminhao e uma moto
caminhao1 = Caminhao("Volvo", "FH 540", 2023, 32.0)
moto1 = Moto("Honda", "CB 500", 2024, 500)

# registrando km no caminhao
print(">> registrando km no caminhão:")
caminhao1.rodar(1500)
caminhao1.rodar(800)

# registrando km na moto
print("\n>> registrando km na moto:")
moto1.rodar(200)
moto1.rodar(350)

# tentando km negativo pra ver o erro
print("\n>> tentando km negativo:")
moto1.rodar(-100)

# exibindo dados de todos (polimorfismo)
print("\n== DADOS DA FROTA ==\n")
frota = [caminhao1, moto1]
for veiculo in frota:
    veiculo.exibir_dados()
    print()
