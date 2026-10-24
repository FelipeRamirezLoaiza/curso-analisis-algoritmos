# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Felipe Ramirez Loaiza · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `af23a11`

Muy buen trabajo: el laboratorio está completo y se nota que entendió el tema.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Identifica el tamaño desde el cual divide y vencerás gana (n = 100) y explica con claridad por qué no gana con pocos datos.
- La comparación con el máximo de un arreglo está bien justificada: combinar cuesta una comparación y el resultado sigue siendo `Θ(n)`.
- Recomienda divide y vencerás y declara la estimación a 1.000.000 de registros sin usar regla de tres lineal.

**Lo que puede mejorar:**
- Varias cifras de la pregunta 3 (por ejemplo 0.000004 s contra 0.000009 s, o la ventaja de ×18,3) no se pueden comprobar en la gráfica ni en una tabla del informe.
- En la estimación usa 1,546 s y 0,01182 s para n = 8000, pero en la pregunta 2 y en la gráfica aparecen 1,48 s y 0,011 s. Use siempre los mismos datos.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término.
- Aplica el método maestro (caso 2) y verifica la condición.
- Justifica bien el `Θ(n²)` de la fuerza bruta con los n(n+1)/2 pares.

**Lo que puede mejorar:**
- Podría nombrar explícitamente la comparación entre `f(n)` y `n^(log_b a)` como la condición del caso 2 al resolver.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos en todos los casos pedidos y en las 20 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos, no llama a la fuerza bruta y no modifica la lista.
- Tiene type hints y docstrings en las funciones.

**Lo que puede mejorar:**
- Falta una línea en blanco entre funciones en `pruebas.py` (deben ser dos).

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 8 tamaños.
- Calcula el factor al duplicar n (×3,89 y ×2,07) y lo contrasta bien con `Θ(n²)` y `Θ(n log n)`.
- Lo que dice de n = 4000 y n = 8000 coincide con la gráfica.

**Lo que puede mejorar:**
- Sus afirmaciones sobre n = 10, 50 y 100 no se pueden comprobar en la gráfica; una tabla con los tiempos medidos las habría respaldado.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura correcta, informe en el orden pedido, gráfica visible, enlaces al código en cada parte, instrucciones de reproducción y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre sin errores y genera la gráfica. Ambos algoritmos coinciden en todas las pruebas que hicimos.

## Para el próximo laboratorio
- Deje siempre dos líneas en blanco entre funciones y verifique que todas tengan docstring con Args y Returns y type hints.
- Incluya una tabla con los tiempos medidos para poder citar valores exactos.
- Use los mismos números en todo el informe.
