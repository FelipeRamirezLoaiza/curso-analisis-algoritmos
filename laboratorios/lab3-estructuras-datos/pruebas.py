import random
from estructuras import ListaEnlazada, TablaHash


def prueba() -> None:
    # 1. Búsqueda básica (exitosa e infructuosa)
    print("=== 1. Busqueda Basica ===")
    lista = ListaEnlazada()
    tabla = TablaHash(10)

    lista.insertar(1000000010, "en bodega")
    tabla.insertar(1000000010, "en bodega")

    # Verificación de búsqueda exitosa
    assert lista.buscar(1000000010) == "en bodega"
    assert tabla.buscar(1000000010) == "en bodega"
    print(f"Guia 1000000010 encontrada -> Lista: '{lista.buscar(1000000010)}' | Tabla: '{tabla.buscar(1000000010)}'")

    # Verificación de búsqueda infructuosa
    assert lista.buscar(9999999999) is None
    assert tabla.buscar(9999999999) is None
    print(f"Guia 9999999999 inexistente -> Lista: {lista.buscar(9999999999)} | Tabla: {tabla.buscar(9999999999)}\n")

    # 2. Colisión forzada (m = 7), longitud de casilla y factor de carga
    print("=== 2. Colision Forzada (m = 7) y Factor de Carga ===")
    tabla_colision = TablaHash(7)
    guias = (10, 24, 17)

    for g in guias:
        assert tabla_colision.hash(g) == 3  # Verifica que caen en la casilla 3
        tabla_colision.insertar(g, "en reparto")
        print(f"Guia {g:2d} insertada en casilla {tabla_colision.hash(g)}")

    # Imprimir estado de la casilla 3
    elementos_casilla_3 = []
    actual = tabla_colision.casillas[3].cabeza
    while actual:
        elementos_casilla_3.append(f"(Guia: {actual.guia}, Estado: '{actual.estado}')")
        actual = actual.siguiente
    print(f"\nContenido [Casilla 3]: {' -> '.join(elementos_casilla_3)}")

    # Verificaciones con assert
    for g in guias:
        assert tabla_colision.buscar(g) == "en reparto"

    assert tabla_colision.casillas[3].tamano == 3
    assert tabla_colision.factor_carga() == 3 / 7

    print(f"Longitud de casilla 3: {tabla_colision.casillas[3].tamano} nodos")
    print(f"Factor de carga (alpha): {tabla_colision.factor_carga():.4f} (3/7)\n")

    # 3. Validación en 20 colecciones aleatorias
    print("=== 3. Validacion en 20 Colecciones Aleatorias ===")
    estados = ["en bodega", "en reparto", "entregado", "cancelado"]

    for i in range(1, 21):
        m = random.randint(5, 50)
        n = random.randint(10, 100)

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        # Generar n guías únicas
        guias_existentes = set()
        while len(guias_existentes) < n:
            guias_existentes.add(random.randint(10**9, 10**10 - 1))

        guias_dict = {}
        for g in guias_existentes:
            estado = random.choice(estados)
            guias_dict[g] = estado
            lista.insertar(g, estado)
            tabla.insertar(g, estado)

        # Probar que guías existentes devuelven el mismo resultado
        guia_m = next(iter(guias_dict))
        lista_exist = lista.buscar(guia_m)
        tabla_exist = tabla.buscar(guia_m)
        assert lista_exist == tabla_exist == guias_dict[guia_m]

        for g, estado in guias_dict.items():
            assert lista.buscar(g) == tabla.buscar(g) == estado

        # Probar que guías inexistentes devuelven None en lista y tabla
        guia_inex = random.randint(10**9, 10**10 - 1)
        while guia_inex in guias_existentes:
            guia_inex = random.randint(10**9, 10**10 - 1)

        lista_inex = lista.buscar(guia_inex)
        tabla_inex = tabla.buscar(guia_inex)
        assert lista_inex is None and tabla_inex is None

        for _ in range(20):
            g_i = random.randint(10**9, 10**10 - 1)
            if g_i not in guias_existentes:
                assert lista.buscar(g_i) is tabla.buscar(g_i) is None

        print(
            f"Coleccion {i}/20 (m={m}, n={n}) -> "
            f"Existente ({guia_m}) -> Lista: '{lista_exist}' / Tabla: '{tabla_exist}' | "
            f"Inexistente ({guia_inex}) -> Lista: '{lista_inex}' / Tabla: '{tabla_inex}' | "
        )


if __name__ == "__main__":
    prueba()