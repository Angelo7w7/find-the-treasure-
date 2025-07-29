# Find the Treasure

¡Bienvenido/a a **Find the Treasure**!  
Este es un pequeño juego de consola en Python donde tu objetivo es encontrar el tesoro escondido sin pisar ninguna bomba.

## ¿Cómo se juega?

- El camino tiene 100 posiciones numeradas del 1 al 100.
- El tesoro (`0`) está oculto en una posición aleatoria.
- Hay 10 bombas (`*`) repartidas aleatoriamente (sin solaparse con el tesoro).
- El jugador (`P`) inicia en la posición 0.
- En cada turno, puedes saltar entre 1 y 5 posiciones.
- Si caes sobre una bomba, ¡pierdes!
- Si llegas al tesoro, ¡ganas!
- Si te pasas de la posición 100, pierdes.

## Ejecución

1. Asegúrate de tener Python 3 instalado.
2. Descarga el archivo `treasure_game.py`.
3. Ejecuta en tu terminal:

   ```bash
   python treasure_game.py
   ```

4. Sigue las instrucciones en pantalla para jugar.

## Ejemplo de partida

```
*** Welcome to the treasure adventure! ***
Your goal is to reach the treasure without stepping on bombs.
Good luck!

P*------*--*--*-------*-------*--*---*---*---*---*--0--*-------
You're at position 0
Choose a number between 1 and 5 to jump
Now jump: 3
You're safe... for now.
---P*------*--*--*-------*-------*--*---*---*---*---*--0--*-------
...
```

## Créditos

Juego desarrollado por [Angelo7w7](https://github.com/Angelo7w7).

---
¡Diviértete y buena suerte buscando el tesoro!
