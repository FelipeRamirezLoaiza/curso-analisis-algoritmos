import random

from subarreglo import (subarreglo_fuerza_bruta, subarreglo_maximo, suma_cruzada,)

def verificar(nombre: str, serie: list[int], suma_esperada: int) -> None:
    """Comprueba ambas funciones contra una suma conocida.

    Ademas valida que los indices devueltos sean coherentes con la suma
    y que la lista original no se modifique. Muestra el resultado.
    """
    copia = list(serie)
    n = len(serie)
    fuerza_bruta = subarreglo_fuerza_bruta(serie)
    divide_venceras = subarreglo_maximo(serie, 0, n - 1)

    for resultado in (fuerza_bruta, divide_venceras):
        inicio, fin, suma = resultado
        assert suma == suma_esperada, (serie, resultado)
        assert 0 <= inicio <= fin < n, (serie, resultado)
        assert sum(serie[inicio : fin + 1]) == suma, (serie, resultado)

    assert serie == copia, "La funcion modifico la lista recibida"
    print(
        f"{nombre}: esperada={suma_esperada} | "
        f"fuerza bruta={fuerza_bruta} | "
        f"divide y venceras={divide_venceras} | OK"
    )


# 1. Serie de ocho dias de la situacion problema.
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17
verificar("Serie de 8 dias", serie, 17)

# 2. Un solo elemento (positivo y negativo).
verificar("Un elemento (+)", [5], 5)
verificar("Un elemento (-)", [-3], -3)

# 3. Todos negativos.
verificar("Todos negativos", [-3, -2, -6, -4], -2)

# 4. Todos positivos.
verificar("Todos positivos", [5, 8, 3, 9], 25)

# 5. El mejor tramo cruza el punto medio (medio = 3 en 0..7).
cruzada = [-5, 2, 6, 7, 3, 4, -8, -1]
assert suma_cruzada(cruzada, 0, 3, 7) == (1, 5, 22)
verificar("Cruza el medio", cruzada, 22)

# 6. Listas aleatorias: ambas funciones deben dar la misma suma.
random.seed(42)
for numero in range(1, 21):
    largo = random.randint(1, 60)
    aleatoria = [random.randint(-20, 20) for _ in range(largo)]
    copia = list(aleatoria)
    suma_fb = subarreglo_fuerza_bruta(aleatoria)[2]
    suma_dv = subarreglo_maximo(aleatoria, 0, largo - 1)[2]
    assert suma_fb == suma_dv, (aleatoria, suma_fb, suma_dv)
    assert aleatoria == copia
    print(
        f"Aleatoria {numero:>2} (n={largo:>2}): "
        f"fb={suma_fb:>4} | dv={suma_dv:>4} | OK"
    )

print("Todas las pruebas pasaron.")