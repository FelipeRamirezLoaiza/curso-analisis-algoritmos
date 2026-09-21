"""Parte 4: comparacion experimental de insertion sort y merge sort (escenario A)."""

import math
import os
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio
from parte3_casos import TAMANOS, CARPETA_GRAFICAS, esta_ordenado_descendente

# Tamanos extra SOLO para merge sort (insertion sort tardaria demasiado):
# sirven para extrapolar el tiempo a 1.200.000 registros.
TAMANOS_EXTRA_MERGE = [25_000, 50_000, 100_000, 200_000]


def medir(algoritmo, datos: list[int]) -> tuple[float, int]:
    """Cronometra unicamente la llamada al algoritmo."""
    inicio = time.perf_counter()
    resultado, comparaciones = algoritmo(datos)
    fin = time.perf_counter()
    assert esta_ordenado_descendente(resultado) and len(resultado) == len(datos)
    return fin - inicio, comparaciones


def experimento_comparativo() -> dict:
    res = {"insertion sort": {"t": [], "c": []}, "merge sort": {"t": [], "c": []}}
    for n in TAMANOS:
        datos = generar_aleatorio(n)  # no se cronometra
        for nombre, alg in (("insertion sort", insertion_sort), ("merge sort", merge_sort)):
            t, c = medir(alg, datos)
            res[nombre]["t"].append(t)
            res[nombre]["c"].append(c)
    return res


def graficar(res: dict) -> None:
    plt.figure(figsize=(8, 5))
    for nombre, v in res.items():
        plt.plot(TAMANOS, v["t"], marker="o", label=nombre)
    plt.xlabel("Tamano de entrada n (numero de registros)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.title("Escenario A (aleatorio): insertion sort vs. merge sort")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "parte4_tiempo.png"), dpi=150)
    plt.close()


def imprimir(res: dict) -> None:
    print(f"{'n':>8} | {'ins. comps':>13} {'ins. t (s)':>11} | {'merge comps':>12} {'merge t (s)':>12}")
    for k, n in enumerate(TAMANOS):
        i, m = res["insertion sort"], res["merge sort"]
        print(f"{n:>8} | {i['c'][k]:>13} {i['t'][k]:>11.5f} | {m['c'][k]:>12} {m['t'][k]:>12.5f}")


def merge_tamanos_grandes() -> None:
    print("\nMerge sort en tamanos grandes (para extrapolar):")
    print(f"{'n':>9} {'comparaciones':>15} {'n*log2(n)':>14} {'tiempo (s)':>11}")
    for n in TAMANOS_EXTRA_MERGE:
        t, c = medir(merge_sort, generar_aleatorio(n))
        print(f"{n:>9} {c:>15} {n * math.log2(n):>14.0f} {t:>11.4f}")


if __name__ == "__main__":
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
    resultados = experimento_comparativo()
    imprimir(resultados)
    graficar(resultados)
    merge_tamanos_grandes()
    print("\nGrafica guardada en graficas/parte4_tiempo.png")
