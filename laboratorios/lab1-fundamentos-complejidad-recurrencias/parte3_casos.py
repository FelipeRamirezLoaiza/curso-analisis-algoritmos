"""Parte 3: peor caso, mejor caso y caso promedio de insertion sort."""

import os
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
CARPETA_GRAFICAS = "graficas"

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}


def esta_ordenado_descendente(lista: list[int]) -> bool:
    """Verifica que la lista quede de mayor a menor (comprobacion de correccion)."""
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            return False
    return True


def medir(algoritmo, datos: list[int]) -> tuple[float, int]:
    """Mide solo la llamada al algoritmo. Retorna (segundos, comparaciones)."""
    inicio = time.perf_counter()
    resultado, comparaciones = algoritmo(datos)
    fin = time.perf_counter()

    assert esta_ordenado_descendente(resultado), "El resultado no quedo ordenado"
    assert len(resultado) == len(datos), "Se perdieron o duplicaron registros"
    return fin - inicio, comparaciones


def ejecutar_experimento() -> dict:
    """Corre insertion sort en los tres escenarios para todos los tamanos."""
    resultados = {nombre: {"tiempo": [], "comparaciones": []} for nombre in ESCENARIOS}

    for n in TAMANOS:
        for nombre, generador in ESCENARIOS.items():
            datos = generador(n)  # la generacion NO se cronometra
            segundos, comps = medir(insertion_sort, datos)
            resultados[nombre]["tiempo"].append(segundos)
            resultados[nombre]["comparaciones"].append(comps)
        print(f"n = {n} listo")

    return resultados


def graficar(resultados: dict, magnitud: str, ylabel: str, titulo: str, archivo: str) -> None:
    """Dibuja los tres escenarios en los mismos ejes y guarda el PNG."""
    plt.figure(figsize=(8, 5))
    for nombre, valores in resultados.items():
        plt.plot(TAMANOS, valores[magnitud], marker="o", label=nombre)
    plt.xlabel("Tamano de entrada (n)")
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(CARPETA_GRAFICAS, archivo), dpi=150)
    plt.close()


def imprimir_tabla(resultados: dict) -> None:
    """Muestra los datos crudos para usarlos en el README."""
    for nombre, valores in resultados.items():
        print(f"\n{nombre}")
        print(f"{'n':>8} {'comparaciones':>16} {'tiempo (s)':>12}")
        for n, c, t in zip(TAMANOS, valores["comparaciones"], valores["tiempo"]):
            print(f"{n:>8} {c:>16} {t:>12.5f}")


if __name__ == "__main__":
    os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
    datos_medidos = ejecutar_experimento()
    imprimir_tabla(datos_medidos)
    graficar(datos_medidos, "comparaciones", "Numero de comparaciones",
             "Insertion sort: comparaciones vs. tamano", "parte3_comparaciones.png")
    graficar(datos_medidos, "tiempo", "Tiempo de ejecucion (s)",
             "Insertion sort: tiempo vs. tamano", "parte3_tiempo.png")
    print("\nGraficas guardadas en graficas/")
