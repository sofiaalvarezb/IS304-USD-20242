
/*
 * Reto #13: Adivina la palabra
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
    
import random

palabras = ["murcielago", "computadora", "programacion", "desarrollo", "tecnologia"]

def seleccionar_palabra(palabras):
    palabra = random.choice(palabras)
    letras_a_ocultar = random.sample(range(len(palabra)), k=int(len(palabra) * 0.4))  # Oculta hasta el 40% de la palabra
    palabra_oculta = ''.join(['_' if i in letras_a_ocultar else letra for i, letra in enumerate(palabra)])
    return palabra, palabra_oculta
