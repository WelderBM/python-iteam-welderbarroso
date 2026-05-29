# Lista 02 — Questão 06: Módulo de Estatísticas (módulo estatísticas)
# Aluno: welder barroso de melo
# Data:  29-05-2026

import math

def media(dados):
    """calcula a media aritmetica de uma lista de numeros"""
    if not dados:
        raise ValueError("a lista ta vazia")
    resultado = sum(dados) / len(dados)
    return round(resultado, 2)

def mediana(dados):
    """calcula a mediana de uma lista de numeros"""
    if not dados:
        raise ValueError("a lista ta vazia")
    ordenado = sorted(dados)
    n = len(ordenado)
    meio = n // 2
    if n % 2 == 0:
        # se a quantidade for par pega os dois do meio e faz a media deles
        resultado = (ordenado[meio - 1] + ordenado[meio]) / 2
    else:
        resultado = ordenado[meio]
    return round(resultado, 2)

def moda(dados):
    """calcula a moda que é o valor que mais aparece na lista"""
    if not dados:
        raise ValueError("a lista ta vazia")
    # conta quantas vezes cada numero aparece
    contagem = {}
    for valor in dados:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
    # acha qual tem mais
    maior_contagem = 0
    valor_moda = dados[0]
    for valor, qtd in contagem.items():
        if qtd > maior_contagem:
            maior_contagem = qtd
            valor_moda = valor
    return valor_moda

def desvio_padrao(dados):
    """calcula o desvio padrao populacional"""
    if not dados:
        raise ValueError("a lista ta vazia")
    med = sum(dados) / len(dados)
    # soma dos quadrados das diferencas
    soma_quadrados = 0
    for valor in dados:
        soma_quadrados += (valor - med) ** 2
    variancia = soma_quadrados / len(dados)
    resultado = math.sqrt(variancia)
    return round(resultado, 2)
