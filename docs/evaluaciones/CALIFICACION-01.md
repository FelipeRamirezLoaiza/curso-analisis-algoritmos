# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Felipe Ramirez Loaiza · **Laboratorio:** Plataforma Tamiza (lab1-fundamentos-complejidad-recurrencias)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `70723ce`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 20 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **80 / 100** |
| **Nota (0–5)** | **4.00** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo, y nombra la restricción que se incumple: la ventana de cuatro horas.
- Explica que el trabajo crece con el cuadrado de los datos (60 veces más registros, unas 3.600 veces más trabajo), por eso un servidor más rápido no resuelve el fondo.
- Da un segundo ejemplo propio (tienda en línea con 500.000 productos y respuesta en menos de 2 segundos).
- Calcula la energía (500 W, 4 horas, unos 730 kWh al año) y presenta dos perjuicios: el paciente de alto riesgo y el operador del centro de contacto, diciendo quién asume el costo.

**Lo que puede mejorar:**
- En la Parte 1 falta decir con claridad que, aunque el servidor fuera el doble de rápido, el tiempo seguiría creciendo igual de rápido al aumentar los registros.
- La Parte 2 trata la obligación sobre el orden de la lista de forma corta; podía profundizar en las consecuencias de llamar primero a la persona equivocada.

## 2. Calidad de la explicación teórica (20 / 25)
**Lo que hizo bien:**
- La Parte 3.1 define los tres casos diciendo sobre qué se toma el máximo, el mínimo y el promedio, justifica usar el peor caso y deja la predicción escrita antes de medir.
- La recurrencia de merge sort está bien explicada término a término y el método maestro está resuelto con `a`, `b`, `f(n)` y la condición verificada: `Θ(n log n)`.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- El análisis línea a línea de insertion sort deja varias filas con "depende del orden de los datos" en lugar de contar cuántas veces se ejecuta cada línea y sumar los costos.
- La tabla de complejidades usa palabras ("Lineal", "Cuadrático") y no la notación `O`, `Θ`.
- Hay un pequeño error de escritura: "0(n)" en vez de `O(n)`.

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista original, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `sort()`. La mezcla de merge sort es propia.
- Los tres generadores dan listas con valores distintos, y la semilla hace los resultados reproducibles. El escenario B queda bien armado (98 % ordenado y 2 % al final).

**Lo que puede mejorar:**
- Algunas funciones no tienen todos los *type hints* o *docstring* (por ejemplo `medir`, `dividir`, `experimento_comparativo`).
- Hay detalles de estilo PEP 8: falta una línea en blanco entre funciones, falta el salto de línea final en `algoritmos.py`, los imports quedan después de código en los scripts y una línea es demasiado larga.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con unidades y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con datos el peor caso (C), el mejor (B) y el parecido al promedio (A), y lo contrasta con su predicción.
- En 4.3 recomienda merge sort, responde sobre el servidor con un dato medido y extrapola a 1.200.000 registros declarando que es una estimación (unas 8,35 horas para insertion sort).

**Lo que puede mejorar:**
- En 4.2 no explica de verdad lo que pasa con los tamaños pequeños; solo dice que la diferencia es menor.
- En 4.3 la discusión de otras consideraciones es breve (solo la memoria extra); podía hablar de la estabilidad o del riesgo de que B deje de ser casi ordenado.
- Las cifras del texto de 4.2 y 4.3 vienen de una corrida distinta a la tabla de la Parte 3; aclare de qué corrida salen los datos.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en un lugar válido, con todos los archivos y las tres gráficas pedidas.
- Las gráficas se ven en el informe y cada parte práctica enlaza su código.
- Hay cinco commits sobre el laboratorio con mensajes descriptivos.

**Lo que puede mejorar:**
- El informe no trae su nombre completo.
- Faltan las instrucciones para reproducir el experimento (activar el entorno y qué comando ejecutar en cada parte).

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en mis pruebas y los scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Ponga su nombre y una sección de instrucciones de reproducción al inicio del informe.
- Complete el análisis línea a línea contando cuántas veces se ejecuta cada línea y sumando.
- Use notación `O`, `Θ`, `Ω` en las tablas de complejidad.
- Agregue *type hints* y *docstring* a todas las funciones y corrija los detalles de PEP 8.
- Explique con datos los comportamientos inesperados de las gráficas, como los tamaños pequeños.
