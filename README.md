
---

# Juego Snake PRO

¡Bienvenido a **Snake PRO**! Este es un juego simple y divertido de Snake, donde controlas una serpiente que debe recoger comida, evitar bombas y sobrevivir sin chocar contra sí misma o los bordes del mapa. Tienes tres vidas, y cada vez que las pierdes, reapareces sin cuerpo.

## Controles
- **Teclas de flecha**: Usa las flechas del teclado para mover la serpiente en las cuatro direcciones (Arriba, Abajo, Izquierda, Derecha).

## Reglas del juego
1. **Vidas**: Empiezas con **3 vidas**.
   - Si pierdes una vida, la serpiente reaparece en el centro del mapa sin cuerpo, pero tu puntuación y la comida permanecerán.
   - Si pierdes todas las vidas, la serpiente se reiniciará por completo: cuerpo, posición y puntuación.
   
2. **Comida**:
   - La serpiente debe comer la comida roja para crecer y ganar puntos.
   - Algunas veces aparecerá una **comida especial** de color rosa (comida plus) que te dará **puntos adicionales**.

3. **Bomba**:
   - Ten cuidado con las bombas negras en forma de tortuga. Si la serpiente las toca, perderás una vida.

4. **Bordes del mapa**:
   - Si la serpiente choca con los bordes de la pantalla, también perderás una vida.

5. **Puntuación**:
   - Gana puntos comiendo comida.
   - Tu puntuación máxima se guarda en el archivo `max_puntuacion.txt` para que puedas intentar superarla en futuras partidas.

## Cómo jugar en Windows (sin necesidad de un entorno de desarrollo)

Sigue estos pasos para jugar en Windows sin necesidad de utilizar un IDE como PyCharm o Visual Studio Code:

### Paso 1: Instalar Python
Antes de jugar, asegúrate de que tienes instalado **Python 3.x** en tu computadora.

1. Descarga Python desde el sitio oficial: [Descargar Python](https://www.python.org/downloads/).
2. Asegúrate de marcar la opción "Add Python to PATH" al momento de instalar.
3. Verifica que Python esté correctamente instalado abriendo la consola de comandos (CMD) y escribiendo:
   ```
   python --version
   ```
   Deberías ver algo como: `Python 3.x.x`.

### Paso 2: Descargar el código del juego
1. Guarda el archivo del juego (el código Python proporcionado) como `snake_pro.py` en una carpeta de tu elección.

### Paso 3: Ejecutar el juego
1. Abre la consola de comandos de Windows (CMD).
2. Navega a la carpeta donde guardaste el archivo `snake_pro.py` usando el comando `cd`. Por ejemplo:
   ```
   cd C:\ruta\de\la\carpeta
   ```
3. Una vez en la carpeta del juego, escribe el siguiente comando para ejecutar el juego:
   ```
   python snake_pro.py
   ```

### ¡Listo!
El juego se abrirá en una nueva ventana, donde podrás comenzar a jugar inmediatamente usando las flechas del teclado. ¡Diviértete recolectando puntos y superando tu mejor puntuación!

---

¡Esperamos que disfrutes de **Snake PRO**!