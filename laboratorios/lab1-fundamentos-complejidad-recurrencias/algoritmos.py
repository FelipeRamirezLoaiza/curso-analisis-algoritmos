"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    a = list(datos)  # copia: no se altera la lista recibida
    comparaciones = 0

    # Orden pedido por Tamiza: de mayor a menor riesgo.
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1  # una comparacion entre dos elementos
            if a[j] < clave:    # estricta: los empates no se cruzan (estable)
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = clave

    return a, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    comparaciones = 0

    def mezclar(izq: list[int], der: list[int]) -> list[int]:
        """Combina dos listas ya ordenadas (mayor a menor) en una sola."""
        nonlocal comparaciones
        resultado = []
        i = j = 0
        while i < len(izq) and j < len(der):
            comparaciones += 1  # una comparacion entre dos elementos
            if izq[i] >= der[j]:  # >= : ante un empate sale primero el de la izquierda (estable)
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
        resultado.extend(izq[i:])  # lo que sobra no requiere comparar
        resultado.extend(der[j:])
        return resultado

    def dividir(lista: list[int]) -> list[int]:
        if len(lista) <= 1:  # caso base
            return lista
        medio = len(lista) // 2
        izq = dividir(lista[:medio])   # conquistar la mitad izquierda
        der = dividir(lista[medio:])   # conquistar la mitad derecha
        return mezclar(izq, der)       # combinar

    return dividir(list(datos)), comparaciones