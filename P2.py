from itertools import permutations

def leer_entrada():
    """
    Lee la entrada del problema desde la entrada estándar.
    Retorna una lista de casos de prueba, donde cada caso es una tupla
    (n, w1, w2, elementos_fundamentales).d
    """
    casos = []
    n_casos = int(input())
    for _ in range(n_casos):
        n, w1, w2 = map(int, input().split())
        elementos_fundamentales = []
        for _ in range(n):
            a1, a2 = map(int, input().split())
            elementos_fundamentales.append((a1, a2))
        casos.append((n, w1, w2, elementos_fundamentales))
    return casos

def calcular_ltp(m1, m2, c1, c2, w1, w2):
    """
    Calcula el LTP necesario para unir dos átomos.
    """
    if c1 == c2:
        return 1 + abs(m1 - m2) % w1
    else:
        return w2 - abs(m1 - m2) % w2

def unir_elementos(elemento_i, elemento_j, w1, w2):
    """
    Intenta unir dos elementos fundamentales siguiendo las reglas del problema.
    Retorna la energía necesaria para unir los dos átomos.
    """
    carga_actual = 1 if elemento_i[1] > 0 else -1
    carga_nueva = 1 if elemento_j[0] > 0 else -1
    return calcular_ltp(abs(elemento_i[1]), abs(elemento_j[0]), carga_actual, carga_nueva, w1, w2)

def construir_compuesto(elementos_fundamentales, w1, w2):
    """
    Intenta construir un compuesto a partir de los elementos fundamentales dados.
    Retorna la energía mínima necesaria si es posible, o "NO SE PUEDE" si no es posible.
    """
    mejor_energia = float('inf')
    mejor_cadena = None

    # Invertir el orden de los elementos dentro de cada tupla en la lista de elementos fundamentales
    elementos_fundamentales = [(b, a) for a, b in elementos_fundamentales]

    for permutacion in permutations(elementos_fundamentales):
        permutacion = list(permutacion)  # Convertir la permutación a una lista
        energia_total = 0
        cadena = []

        for i in range(len(permutacion) - 1):
            energia = unir_elementos(permutacion[i], permutacion[i + 1], w1, w2)
            if energia is None:
                break
            else:
                energia_total += energia
                cadena.append(permutacion[i])

        else:
            cadena.append(permutacion[-1])  # Añadir el último elemento
            if energia_total < mejor_energia:
                mejor_energia = energia_total
                mejor_cadena = cadena

    if mejor_cadena is None:
        return "NO SE PUEDE"
    else:
        # Invertir nuevamente el orden de los elementos dentro de cada tupla en la cadena resultante
        mejor_cadena = [(b, a) for a, b in mejor_cadena]
        cadena_resultado = ",".join(f"({a},{b})" for a, b in mejor_cadena) + " " + str(mejor_energia)
        return cadena_resultado

def main():
    casos = leer_entrada()
    for caso in casos:
        n, w1, w2, elementos_fundamentales = caso
        resultado = construir_compuesto(elementos_fundamentales, w1, w2)
        print(resultado)

if __name__ == "__main__":
    main()
