"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random

# El orden que produce el algoritmo es de mayor a menor.


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    lote = list(range(n))
    rng.shuffle(lote)
    return lote


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    rng = random.Random(semilla)
    n_cola = n - int(n * 0.98)          # el 2% nuevo del dia
    cola = rng.sample(range(n), n_cola)  # valores elegidos al azar
    en_cola = set(cola)

    # El 98% restante, ya en el orden de salida (mayor a menor),
    # construido sin usar ninguna funcion de ordenamiento.
    cabeza = [v for v in range(n - 1, -1, -1) if v not in en_cola]

    return cabeza + cola  # `cola` ya sale en orden aleatorio


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    # El algoritmo produce mayor -> menor, asi que el inverso es menor -> mayor.
    return list(range(n))
