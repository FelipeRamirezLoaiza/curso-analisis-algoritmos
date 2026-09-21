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
