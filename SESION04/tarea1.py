
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

def jugar():
    palabra, palabra_oculta = seleccionar_palabra(palabras)
    intentos = 5 
    print("¡Bienvenido al juego de adivina la palabra!")
    print(f"La palabra es: {palabra_oculta}")
    
    while intentos > 0:
        respuesta = input(f"Tienes {intentos} intentos. Introduce una letra o la palabra completa: ").lower()
        
        if len(respuesta) == len(palabra):
            if respuesta == palabra:
                print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
                return
            else:
                print("Palabra incorrecta.")
                intentos -= 1
                      
        elif len(respuesta) == 1:
            letra = respuesta
            if letra in palabra:
                palabra_oculta = ''.join([letra if palabra[i] == letra else palabra_oculta[i] for i in range(len(palabra))])
                print(f"¡Acertaste! La palabra ahora es: {palabra_oculta}")
            else:
                print("Letra incorrecta.")
                intentos -= 1
            
            if palabra_oculta == palabra:
                print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
                return
        
        else:
            print("Entrada inválida, debes introducir una letra o intentar adivinar la palabra completa.")
        
    print(f"Lo siento, te quedaste sin intentos. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()
