"""Medicion de tiempos de busqueda y generacion de graficas."""

import random
import time
from pathlib import Path
import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

# Rutas absolutas vinculadas
DIR_ACTUAL = Path(__file__).resolve().parent
DIR_GRAFICAS = DIR_ACTUAL / "graficas"


def generar_guias_inexistentes(existentes: set[int], cantidad: int, semilla: int = 7) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: Guias almacenadas en las estructuras.
        cantidad: Cuantas guias inexistentes generar.
        semilla: Semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias_existentes(n: int, semilla: int = 42) -> set[int]:
    """Genera un conjunto de n guias unicas de 10 digitos.

    Args:
        n: Cantidad de guias a generar.
        semilla: Semilla para reproducibilidad.

    Returns:
        Un conjunto con n guias de 10 digitos.
    """
    azar = random.Random(semilla)
    existentes: set[int] = set()
    while len(existentes) < n:
        existentes.add(azar.randint(10**9, 10**10 - 1))
    return existentes


def obtener_primo_cercano(val: int) -> int:
    """Devuelve el numero primo mayor o igual a val mas cercano."""
    def es_primo(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    m = max(2, val)
    while not es_primo(m):
        m += 1
    return m


def experimento_a() -> None:
    """Experimento A: Compara tiempo de busqueda de ListaEnlazada vs TablaHash."""
    valores_n = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    print("--- Ejecutando Experimento A (Lista vs Tabla) ---")

    for n in valores_n:
        guias = generar_guias_existentes(n, semilla=42)
        m = obtener_primo_cercano(n // 2)

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        for guia in guias:
            lista.insertar(guia, "en bodega")
            tabla.insertar(guia, "en bodega")

        # Verificacion interna de equivalencia
        muestra = list(guias)[: min(10, n)]
        for g in muestra:
            assert lista.buscar(g) == tabla.buscar(g) == "en bodega"

        inexistentes = generar_guias_inexistentes(guias, 200, semilla=7)

        # Medir ListaEnlazada
        inicio = time.perf_counter()
        for g_inex in inexistentes:
            lista.buscar(g_inex)
        fin = time.perf_counter()
        tiempo_medio_lista = ((fin - inicio) / 200) * 1e6

        # Medir TablaHash
        inicio = time.perf_counter()
        for g_inex in inexistentes:
            tabla.buscar(g_inex)
        fin = time.perf_counter()
        tiempo_medio_tabla = ((fin - inicio) / 200) * 1e6

        tiempos_lista.append(tiempo_medio_lista)
        tiempos_tabla.append(tiempo_medio_tabla)

        print(
            f"n = {n} | Lista: {tiempo_medio_lista:8.2f} us | "
            f"Tabla (m={m}, alpha={tabla.factor_carga():.2f}): {tiempo_medio_tabla:6.2f} us"
        )

    # Graficar
    plt.figure(figsize=(9, 6))
    plt.plot(valores_n, tiempos_lista, marker="o", label="Lista Enlazada (Θ(n))", color="crimson")
    plt.plot(valores_n, tiempos_tabla, marker="s", label="Tabla Hash (α ≈ 2)", color="royalblue")

    plt.title("Experimento A: Tiempo Medio de Búsqueda de Guías Inexistentes", fontsize=12)
    plt.xlabel("Número de Guías en el Sistema (n)", fontsize=10)
    plt.ylabel("Tiempo Medio por Búsqueda (µs)", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=10)
    plt.tight_layout()

    DIR_GRAFICAS.mkdir(parents=True, exist_ok=True)
    plt.savefig(DIR_GRAFICAS / "lista_vs_tabla.png", dpi=300)
    plt.close()


def experimento_b() -> None:
    """Experimento B: Mide el efecto del factor de carga (alpha) en TablaHash."""
    n_fijo = 20000
    factores_alfa_objetivo = [0.25, 0.5, 1.0, 2.0, 4.0, 10.0]

    guias = generar_guias_existentes(n_fijo, semilla=123)
    inexistentes = generar_guias_inexistentes(guias, 200, semilla=7)

    alfas_reales: list[float] = []
    tiempos_tabla: list[float] = []

    print()
    print("--- Ejecutando Experimento B (Efecto del Factor de Carga alpha) ---")

    for alfa in factores_alfa_objetivo:
        m_ideal = int(n_fijo / alfa)
        m = obtener_primo_cercano(m_ideal)

        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "en reparto")

        alfa_real = tabla.factor_carga()

        inicio = time.perf_counter()
        for g_inex in inexistentes:
            tabla.buscar(g_inex)
        fin = time.perf_counter()
        tiempo_medio = ((fin - inicio) / 200) * 1e6

        alfas_reales.append(alfa_real)
        tiempos_tabla.append(tiempo_medio)

        print(
            f"alpha deseado = {alfa:5.2f} | alpha real = {alfa_real:5.2f} (m = {m:5d}) | "
            f"Tiempo medio: {tiempo_medio:6.2f} us"
        )

    # Graficar
    plt.figure(figsize=(9, 6))
    plt.plot(
        alfas_reales,
        tiempos_tabla,
        marker="^",
        color="darkgreen",
        linewidth=2,
        label="Tabla Hash (n = 20.000)",
    )

    plt.title("Experimento B: Tiempo de Búsqueda vs. Factor de Carga (α)", fontsize=12)
    plt.xlabel("Factor de Carga α (n / m)", fontsize=10)
    plt.ylabel("Tiempo Medio por Búsqueda (µs)", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=10)
    plt.tight_layout()

    DIR_GRAFICAS.mkdir(parents=True, exist_ok=True)
    plt.savefig(DIR_GRAFICAS / "tiempo_vs_alfa.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    experimento_a()
    experimento_b()