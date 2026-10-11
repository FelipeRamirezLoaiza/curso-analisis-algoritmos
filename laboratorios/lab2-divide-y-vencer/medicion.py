"""Medicion del tiempo de ejecucion: fuerza bruta vs divide y venceras."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

SEMILLA = 42
TAMANIOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 3
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_entrada(n: int) -> list[int]:
    """Genera una serie de n variaciones diarias de caja.

    Args:
        n: cantidad de dias de la serie.

    Returns:
        Lista de n enteros aleatorios entre -100 y 100.
    """
    return [random.randint(-100, 100) for _ in range(n)]


def cronometrar_fuerza_bruta(valores: list[int]) -> tuple[float, float]:
    """Mide una ejecucion de la fuerza bruta sobre la serie dada.

    Args:
        valores: serie de variaciones diarias.

    Returns:
        Una tupla (segundos, suma) con el tiempo de la llamada y la suma
        maxima encontrada.
    """
    inicio_reloj = time.perf_counter()
    _, _, suma = subarreglo_fuerza_bruta(valores)
    fin_reloj = time.perf_counter()
    return fin_reloj - inicio_reloj, suma


def cronometrar_divide_venceras(valores: list[int]) -> tuple[float, float]:
    """Mide una ejecucion del divide y venceras sobre la serie dada.

    Args:
        valores: serie de variaciones diarias.

    Returns:
        Una tupla (segundos, suma) con el tiempo de la llamada y la suma
        maxima encontrada.
    """
    inicio_reloj = time.perf_counter()
    _, _, suma = subarreglo_maximo(valores, 0, len(valores) - 1)
    fin_reloj = time.perf_counter()
    return fin_reloj - inicio_reloj, suma


def ejecutar_experimento() -> tuple[list[float], list[float]]:
    """Mide ambos algoritmos para cada tamanio de TAMANIOS.

    Para cada n genera una sola lista (con semilla fija) y se la entrega
    a los dos algoritmos. Cada algoritmo se ejecuta REPETICIONES veces
    sobre esa lista y se conserva el menor tiempo, que es el menos
    afectado por otros procesos del sistema. Solo se cronometra la
    llamada al algoritmo, nunca la generacion de datos.

    Returns:
        Una tupla (tiempos_fuerza_bruta, tiempos_divide_venceras) en
        segundos, alineadas con TAMANIOS.

    Raises:
        AssertionError: si en algun tamanio los algoritmos no devuelven
            la misma suma.
    """
    random.seed(SEMILLA)
    tiempos_fuerza_bruta: list[float] = []
    tiempos_divide_venceras: list[float] = []

    for n in TAMANIOS:
        valores = generar_entrada(n) #Se genera una vez por tamaño

        mejor_fb = float("inf")
        mejor_dv = float("inf")
        for _ in range(REPETICIONES):
            segundos_fb, suma_fb = cronometrar_fuerza_bruta(valores)
            segundos_dv, suma_dv = cronometrar_divide_venceras(valores)
            assert suma_fb == suma_dv, (
                f"Sumas distintas para n={n}: {suma_fb} vs {suma_dv}"
            )
            mejor_fb = min(mejor_fb, segundos_fb)
            mejor_dv = min(mejor_dv, segundos_dv)

        tiempos_fuerza_bruta.append(mejor_fb)
        tiempos_divide_venceras.append(mejor_dv)
        print(
            f"n={n:>5}  fuerza bruta={mejor_fb:>10.6f} s  "
            f"divide y venceras={mejor_dv:>10.6f} s  "
            f"cociente={mejor_fb / mejor_dv:>7.1f}x  (sumas iguales: {suma_fb})"
        )

    return tiempos_fuerza_bruta, tiempos_divide_venceras


def graficar_tiempos(tamanios: list[int],tiempos_fuerza_bruta: list[float],tiempos_divide_venceras: list[float],ruta: Path) -> None:
    """Grafica tiempo vs tamanio de entrada con ambas curvas.

    Args:
        tamanios: tamanios de entrada medidos.
        tiempos_fuerza_bruta: tiempos de la fuerza bruta, en segundos.
        tiempos_divide_venceras: tiempos del divide y venceras, en segundos.
    """
    ruta.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.plot(tamanios, tiempos_fuerza_bruta, marker="o", label="Fuerza bruta")
    plt.plot(tamanios, tiempos_divide_venceras, marker="o", label="Divide y venceras",)
    plt.title("Subarreglo maximo: tiempo de ejecucion vs tamanio de entrada")
    plt.xlabel("Tamanio de la entrada n (numero de dias)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig(ruta, dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    tiempos_fuerza_bruta, tiempos_divide_vencer = ejecutar_experimento()
    graficar_tiempos(TAMANIOS, tiempos_fuerza_bruta, tiempos_divide_vencer, CARPETA_GRAFICAS / "tiempo_vs_n.png")
    print(f"Grafica guardada en {CARPETA_GRAFICAS}")
