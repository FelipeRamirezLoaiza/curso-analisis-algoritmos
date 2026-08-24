def calcular_promedio(numeros: list[int | float]) -> float:
    """Calcula el promedio aritmético de una lista de números.

    Args:
        numeros (list[int | float]): Lista con valores numéricos.

    Returns:
        float: El promedio aritmético de los elementos de la lista.
    """
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)


def main() -> None:
    lista_numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(lista_numeros)
    print(promedio)


if __name__ == "__main__":
    main()