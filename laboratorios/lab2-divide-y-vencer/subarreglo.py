"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    La suma se acumula dentro del ciclo interno en vez de recalcularse
    desde cero para cada par, lo que da un costo de Θ(n²).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    n = len(valores)
    mejor_inicio, mejor_fin = 0, 0
    suma_maxima = float("-inf")

    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += valores[j]
            if suma > suma_maxima:
                suma_maxima = suma
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, suma_maxima


def suma_cruzada(valores: list[float], inicio: int, medio: int, fin: int) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Hace un barrido lineal hacia la izquierda desde `medio` y otro hacia
    la derecha desde `medio + 1`, y suma el mejor extremo de cada lado.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    suma = 0
    suma_maxima_izquierda = float("-inf")
    mejor_izquierda = medio
    for i in range(medio, inicio-1, -1):
        suma += valores[i]
        if suma > suma_maxima_izquierda:
            suma_maxima_izquierda = suma
            mejor_izquierda = i

    suma = 0
    suma_maxima_derecha = float("-inf")
    mejor_derecha = medio+1
    for j in range(medio+1, fin+1):
        suma += valores[j]
        if suma > suma_maxima_derecha:
            suma_maxima_derecha = suma
            mejor_derecha = j

    return (mejor_izquierda, mejor_derecha, suma_maxima_izquierda + suma_maxima_derecha)


def subarreglo_maximo(valores: list[float], inicio: int, fin: int) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.

    Divide el rango en dos mitades y devuelve el mejor de tres casos:
    izquierdo, derecho y cruzado. Su recurrencia es
    T(n) = 2T(n/2) + Θ(n), es decir, Θ(n log n).

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    inicio_izquierda, fin_izquierda, suma_izquierda = subarreglo_maximo(valores, inicio, medio)
    inicio_derecha, fin_derecha, suma_derecha = subarreglo_maximo(valores, medio + 1, fin)
    inicio_cruzado, fin_cruzado, suma_cruzado = suma_cruzada(valores, inicio, medio, fin)

    if suma_izquierda >= suma_derecha and suma_izquierda >= suma_cruzado:
        return inicio_izquierda, fin_izquierda, suma_izquierda
    if suma_derecha >= suma_izquierda and suma_derecha >= suma_cruzado:
        return inicio_derecha, fin_derecha, suma_derecha
    return inicio_cruzado, fin_cruzado, suma_cruzado
