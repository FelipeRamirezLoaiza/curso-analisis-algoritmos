# Retroalimentación — Lab 03: Estructuras de datos

**Estudiante:** Felipe Ramírez Loaiza · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `6212de7`

Muy buen trabajo: las estructuras funcionan y el análisis es sólido.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Explica bien la colisión con el ejemplo de 10, 24 y 17 con m = 7.
- Justifica por qué la tabla hash no sirve para rangos y estima la altura (399.999) y las comparaciones (~200.000) del árbol degenerado frente a ~19 del equilibrado.
- Recomienda una combinación coherente: tabla hash para la consulta puntual y árbol autobalanceado para rangos.

**Lo que puede mejorar (y cómo corregirlo):**
- No explica por qué hay colisiones aunque la tabla tenga más casillas que guías.
  → *Cómo corregirlo:* piense cuántas guías posibles (diez dígitos) hay frente a cuántas casillas, y qué pasa cuando dos guías distintas dejan el mismo residuo.
- La estimación a 5.000.000 de envíos no se declara claramente como estimación ni se explica por qué la forma de la curva permite extrapolar.
  → *Cómo corregirlo:* diga explícitamente que es una estimación y justifique, con lo que muestra su gráfica, por qué la curva de cada estructura permite proyectar ese valor.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla, nombra el supuesto de dispersión uniforme y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista con costo `Θ(n)`.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Lista y tabla devuelven el estado correcto en búsquedas exitosas e infructuosas; la colisión en la casilla 3 y el factor de carga 3/7 se verifican con `assert`.
- La tabla reutiliza la lista, no usa `dict`, `set` ni `hash()`, y la búsqueda es iterativa.
- Prueba 20 colecciones aleatorias comparando lista y tabla.

**Lo que puede mejorar (y cómo corregirlo):**
- La función `obtener_primo_cercano` y su función interna `es_primo` no tienen docstring completo con `Args` y `Returns`, ni *type hints* en la interna.
  → *Cómo corregirlo:* agregue secciones `Args:` y `Returns:` en el estilo Google y anote los tipos de `es_primo`.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera usa seis valores de `n` y la segunda seis de `α`.
- Calcula el factor de crecimiento de la lista entre 20.000 y 50.000 (de ~750 µs a ~2.100 µs), coherente con lo que se ve en la gráfica.

**Lo que puede mejorar (y cómo corregirlo):**
- Dice que el tiempo crece de forma "estrictamente lineal" con `α`, pero en la gráfica sube poco hasta α = 2, da un salto fuerte en α = 4 (~0,47 µs) y luego sube más despacio hasta α = 10 (~0,59 µs).
  → *Cómo corregirlo:* describa la forma real de la curva con valores leídos de la gráfica y discuta qué tanto se parece a `Θ(1 + α)`, considerando el ruido de medir fracciones de microsegundo.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- Carpeta en ubicación válida (`laboratorios/lab3-estructuras-datos/`), con todos los archivos pedidos, enlaces al código, instrucciones de reproducción y cinco commits descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- Las gráficas no están incrustadas: solo hay un enlace de texto hacia cada PNG, así que no se ven dentro del informe.
  → *Cómo corregirlo:* use la sintaxis de imagen, por ejemplo `![Lista vs Tabla](graficas/lista_vs_tabla.png)`.
- En las instrucciones de reproducción el bloque de código del entorno virtual queda sin cerrar, y eso desordena la vista del README.
  → *Cómo corregirlo:* cierre el bloque con tres comillas invertidas después del comando de activación.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores, y la medición corre completa y genera las dos gráficas.
