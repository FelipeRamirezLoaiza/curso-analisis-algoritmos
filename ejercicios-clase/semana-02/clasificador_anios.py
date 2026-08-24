"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).

    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese años separados por comas (ej. 2026, 1950, 2020): ")
        try:
            # Separamos por coma, quitamos espacios y convertimos cada elemento a int
            anios = [int(anio.strip()) for anio in entrada.split(",") if anio.strip()]
            if not anios:
                print("Error: Debe ingresar al menos un número. Intente de nuevo.\n")
                continue
            return anios
        except ValueError:
            print("Error: Todos los valores deben ser números enteros válidos. Intente de nuevo.\n")


def main() -> None:
    anios_ingresados = leer_anios()

    # Comprensión de listas para filtrar solo los bisiestos
    bisiestos = [anio for anio in anios_ingresados if es_bisiesto(anio)]

    # Resumen de resultados
    print("\n--- Resumen ---")
    print(f"Años evaluados: {anios_ingresados}")
    print(f"Años bisiestos encontrados: {bisiestos}")
    print(f"Total de años bisiestos: {len(bisiestos)}")


if __name__ == "__main__":
    main()