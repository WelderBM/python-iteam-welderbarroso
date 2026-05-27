# Desafio 07 — Bio-Calculadora
# Aluno: (welder barroso de melo)
# Data:  (27-05-2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
from funcoes_mat import area_circulo, volume_esfera, calcular_hipotenusa

while True:
    # Exibe o menu de opções
    print("\n--- MENU DE CÁLCULOS GEOMÉTRICOS ---")
    print("1. Calcular Área do Círculo")
    print("2. Calcular Volume da Esfera")
    print("3. Calcular Hipotenusa")
    print("4. Sair do Programa")
    
    opcao = input("\nEscolha uma opção (1-4): ").strip()

    # O "match" funciona exatamente como o switch-case de outras linguagens
    match opcao:
        case "1":
            raio = float(input("Digite o raio do círculo: "))
            resultado = area_circulo(raio)
            print(f"-> A área do círculo é: {resultado:.2f}")

        case "2":
            raio = float(input("Digite o raio da esfera: "))
            resultado = volume_esfera(raio)
            print(f"-> O volume da esfera é: {resultado:.2f}")

        case "3":
            cateto_a = float(input("Digite o valor do primeiro cateto: "))
            cateto_b = float(input("Digite o valor do segundo cateto: "))
            resultado = calcular_hipotenusa(cateto_a, cateto_b)
            print(f"-> A hipotenusa é: {resultado:.2f}")

        case "4":
            print("Encerrando o programa... Até mais!")
            break  # Quebra o loop 'while' e finaliza o script

        case _:
            # O underline '_' funciona como o 'default', capturando qualquer entrada inválida
            print("Opção inválida! Por favor, digite um número de 1 a 4.")
