# Projeto Integrador — Urna Eletrônica
# Aluno: welder barroso de melo
# Turma: Vespertino 2026

# dicionario que guarda os candidatos cadastrados
candidatos = {}
# lista pra guardar os votos (so o numero, sem identificar quem votou)
votos_registrados = []

def cadastrar_candidato():
    print("digite o numero do candidato")
    numero = input("")
    if numero in candidatos:
        print("esse numero ja ta cadastrado")
        return
    print("digite o nome do candidato")
    nome = input("")
    candidatos[numero] = {"nome": nome, "votos": 0}
    print(f"candidato {nome} ({numero}) cadastrado com sucesso")

def listar_candidatos():
    if not candidatos:
        print("nenhum candidato cadastrado ainda")
        return
    print("\n--- CANDIDATOS ---")
    for numero, dados in candidatos.items():
        print(f"  {numero} - {dados['nome']}")

def votar():
    if not candidatos:
        print("nao tem candidato cadastrado ainda, cadastre antes de votar")
        return

    print("\n========================================")
    print("         URNA ELETRÔNICA")
    print("========================================")
    listar_candidatos()
    print("  0 - Voto em Branco")
    print("========================================")

    print("\ndigite o numero do candidato")
    voto = input("")

    if voto == "0":
        votos_registrados.append("branco")
        print("\nvoto em branco registrado")
    elif voto in candidatos:
        candidatos[voto]["votos"] += 1
        votos_registrados.append(voto)
        print(f"\nvoto registrado para {candidatos[voto]['nome']}")
    else:
        votos_registrados.append("nulo")
        print("\nnumero invalido — voto nulo registrado")

    print("========================================")

def apurar_resultado():
    if not votos_registrados:
        print("nenhum voto foi registrado ainda")
        return

    total = len(votos_registrados)
    brancos = votos_registrados.count("branco")
    nulos = votos_registrados.count("nulo")
    validos = total - brancos - nulos

    print("\n========================================")
    print("        RESULTADO DA ELEIÇÃO")
    print("========================================")
    print(f"total de votos: {total}")
    print(f"votos validos: {validos}")
    print(f"votos em branco: {brancos}")
    print(f"votos nulos: {nulos}")
    print("----------------------------------------")

    # ordena os candidatos por quantidade de votos pra mostrar quem ta na frente
    ranking = sorted(candidatos.items(), key=lambda x: x[1]["votos"], reverse=True)

    for numero, dados in ranking:
        if validos > 0:
            percentual = (dados["votos"] / validos) * 100
        else:
            percentual = 0
        print(f"  {dados['nome']} ({numero}): {dados['votos']} votos ({percentual:.1f}%)")

    # ve quem ganhou
    if ranking and validos > 0:
        vencedor = ranking[0]
        # verifica empate
        empatados = [c for c in ranking if c[1]["votos"] == vencedor[1]["votos"]]
        if len(empatados) > 1:
            nomes = ", ".join([c[1]["nome"] for c in empatados])
            print(f"\nempate entre: {nomes}")
        else:
            print(f"\nvencedor: {vencedor[1]['nome']} com {vencedor[1]['votos']} votos")
    
    print("========================================")

# menu principal
def main():
    while True:
        print("\n===== URNA ELETRÔNICA =====")
        print("1. Cadastrar candidato")
        print("2. Listar candidatos")
        print("3. Votar")
        print("4. Apurar resultado")
        print("5. Encerrar")

        opcao = input("\nopcao: ")

        if opcao == "1":
            cadastrar_candidato()
        elif opcao == "2":
            listar_candidatos()
        elif opcao == "3":
            votar()
        elif opcao == "4":
            apurar_resultado()
        elif opcao == "5":
            print("encerrando a urna...")
            break
        else:
            print("opcao invalida")

main()
