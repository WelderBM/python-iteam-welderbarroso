import math

def area_circulo(raio):
    """Calcula a área de um círculo com base no seu raio.

    Argumentos:
    raio (float): O comprimento do raio do círculo.

    Retorna:
    float: A área total do círculo.
    """
    return math.pi * (raio ** 2)


def volume_esfera(raio):
    """Calcula o volume tridimensional de uma esfera.

    Argumentos:
    raio (float): O comprimento do raio da esfera.

    Retorna:
    float: O volume total da esfera.
    """
    return (4 / 3) * math.pi * (raio ** 3)


def calcular_hipotenusa(cateto_a, cateto_b):
    """Calcula a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras.

    Argumentos:
    cateto_a (float): O comprimento do primeiro cateto.
    cateto_b (float): O comprimento do segundo cateto.

    Retorna:
    float: O comprimento da hipotenusa.
    """
    return math.hypot(cateto_a, cateto_b)
