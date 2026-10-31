# Laboratorio 03: Estructuras de Datos

**Autor:** Felipe Ramírez Loaiza

## Instrucciones para reproducir el experimento

1. **Requisitos previos:** Asegúrese de tener instalado Python.
2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   # venv\Scripts\activate   # En Windows

Si es la primera vez, instale las dependencias con `pip install -r requirements.txt`. Luego entre a /laboratorios/lab3-estructuras-datos y ejecute:

```bash
python pruebas.py     # ejecuta las pruebas construidas.
python medicion.py    # guarda las graficas del laboratorio.
```

## Parte 1: Verificación de Estructuras

Código: [`estructuras.py`](estructuras.py) | [`pruebas.py`](pruebas.py)

* **Búsqueda básica:** Se comprobó la inserción y consulta tanto en la ListaEnlazada como en la TablaHash. Se validaron las búsquedas exitosas retornando el estado correcto de la guía y las búsquedas infructuosas retornando `None`.

* **Colisiones forzadas y factor de carga:** Se configuró una TablaHash con m = 7 casillas y se insertaron las guías 10, 24 y 17. Se verificó manualmente con `assert` que las tres guías colisionaran en la casilla 3 (k mod 7 = 3), que la longitud de dicha casilla fuera de 3 nodos y que el factor de carga resultante fuera exactamente α = 3/7.

* **Validación de equivalencia aleatoria:** Se ejecutaron pruebas sobre 20 colecciones aleatorias con m entre 5 y 50 y n entre 10 y 100. Se validó que para cada guía existente ambas estructuras retornaran exactamente el mismo estado, y que para 20 guías inexistentes por colección ambas retornaran `None`.

## Parte 2: Medición y Gráficas

Código: [`medicion.py`](medicion.py)

Las mediciones se realizaron utilizando el temporizador `time.perf_counter()`, enfocándose en el caso crítico operacional: la búsqueda de guías inexistentes.

* **Experimento A (Lista vs. Tabla):** Se evaluaron 6 tamaños de colecciones (n en [100, 500, 1000, 5000, 20000, 50000]). Para cada n, se configuró la tabla hash con m igual al menor número primo mayor o igual a n / 2, garantizando un factor de carga α ≈ 2. Para cada n, se ejecutaron 200 búsquedas infructuosas y se calculó el tiempo medio en microsegundos (µs).

Gráfica 1: [Lista vs Tabla](graficas/lista_vs_tabla.png)

* **Experimento B (Efecto del factor de carga α):** Se fijó n = 20.000 guías y se varió m para obtener valores de α entre 0.25 y 10.0 ([0.25, 0.5, 1.0, 2.0, 4.0, 10.0]). Se midió el tiempo medio de 200 búsquedas infructuosas para cada configuración.

Gráfica 2: [Tiempo vs Alfa](graficas/tiempo_vs_alfa.png)

## Parte 3: Análisis

### 1. Costo Teórico
En una lista enlazada, buscar una guía inexistente exige recorrer los n nodos desde la cabeza hasta encontrar `None`, realizando n comparaciones, por esto, la complejidad es Θ(n). En la tabla hash con encadenamiento, el costo promedio es Θ(1 + α) donde Θ(1) representa el cálculo de la función hash h(k) = k mod m y el acceso directo al arreglo de casillas, mientras que α = n/m representa la longitud promedio de las listas encadenadas que se deben recorrer.

Este resultado se sostiene bajo el supuesto de dispersión uniforme simple, el cual establece que cualquier clave tiene la misma probabilidad de ser asignada a cualquiera de las m casillas, independientemente de dónde cayeran las demás. Si este supuesto falla y todas las guías caen en la misma casilla, la tabla hash degenera en una única lista enlazada, elevando la complejidad de búsqueda al peor caso: Θ(n).

### 2. Lo Medido contra lo Esperado
* **Experimento A (Tiempo vs. n):** Al analizar dos valores consecutivos como n_1 = 20.000 y n_2 = 50.000 (un factor de incremento de
2.5×):
  * **Lista Enlazada:** El tiempo medio aumentó de aproximadamente 750 µs a 2.100 µs (un incremento de ~2.8×, muy cercano a la relación ideal de 2.5×), confirmando la proporcionalidad lineal teórica Θ(n).
  * **Tabla Hash (α ≈ 2):** El tiempo se mantuvo prácticamente plano (alrededor de 0.25µs a 0.27µs), validando la cota constante Θ(1).
* **Experimento B (Tiempo vs. α):** En la segunda gráfica, al fijar n = 20.000 e incrementar α desde 0.25 hasta 10.0, el tiempo creció de forma estrictamente lineal respecto a α. Esto concuerda con Θ(1 + α), ya que a mayor factor de carga, más nodos hay que recorrer dentro de la lista de la casilla correspondiente.

### 3. Manejo de Colisiones
Una colisión ocurre cuando dos o más claves distintas producen el mismo índice al evaluarse en la función hash (h(k₁) = h(k₂)). Y es lo que ocurre en el ejercicio realizado con m = 7, las guías 10, 24 y 17 colisionan en la casilla 3, porque 10 mod 7 = 3,
24 mod 7 = 3 y 17 mod 7 = 3.

* **Encadenamiento (Chaining):** Mantiene una lista enlazada en cada casilla y tiene como ventaja que no se llena nunca
(α puede ser > 1) y elimina el borrado complejo, pero usa memoria adicional para los punteros de los nodos.

* **Direccionamiento Abierto (Open Addressing):** Guarda todos los elementos dentro de la misma tabla mediante sondeos (probing), este metodo tiene una alta eficiencia de memoria al no usar nodos ni punteros extras, pero si tiene una degradación severa del rendimiento cuando α → 1 y una necesidad de rehash.

### 4. Tabla Hash vs. Árbol de Búsqueda Binario (BST)
Para monitoreo por rango (guías entre X y Y), la tabla hash no sirve porque la función hash por división dispersa pseudoaleatoriamente los elementos, destruye todo orden topológico natural y para responder a un rango se tendría que inspeccionar la totalidad de las m casillas (Θ(m + n)).

Un BST mantiene las claves ordenadas implícitamente, permitiendo ubicar el límite inferior en O(log n) y realizar un recorrido en orden hasta el límite superior en O(log n + k), donde k es el número de elementos devueltos.

Si las 400.000 guías llegaran ya ordenadas de forma secuencial y se insertaran una a una en un BST no balanceado tradicional:
* El árbol degeneraría en una línea recta (equivalente a una lista enlazada).
* **Altura:** h = 399.999.
* **Comparaciones:** Requeriría un promedio de ≈ 200.000 comparaciones por búsqueda.
* **Árbol equilibrado:** Un árbol equilibrado mantendría una altura de h = ⌈log₂(400.000)⌉ ≈ 19 niveles, resolviendo cualquier búsqueda en máximo 19 comparaciones.

## 5. Concepto Técnico para la Jefa de Operaciones
Se recomienda un enfoque híbrido.
1. **Para la consulta puntual del call center:** Una Tabla Hash con encadenamiento mantendrá respuestas instantáneas en tiempo constante.
2. **Para el monitoreo por rangos:** Un Árbol Auto-balanceado (Red-Black / AVL) mantendrá las guías ordenadas con costo de rango O(log n + k).

Para la estimación de 5.000.000 de envíos con búsqueda de una guía inexistente.
* **En Lista Enlazada:** Como la búsqueda infructuosa escala linealmente Θ(n), al multiplicar la carga de 50.000 a 5.000.000 (100×), el tiempo medio medido pasará de ≈ 2.12 ms a aproximadamente 212 ms por consulta.

* **En Tabla Hash (manteniendo α ≈ 2 reajustando m):** Al ser de complejidad constante Θ(1 + α), el tiempo permanece independiente de n. Basado en las mediciones del laboratorio, la respuesta tomará aproximadamente 0.25 µs a 0.30 µs, logrando que la consulta sea imperceptible para los operadores.