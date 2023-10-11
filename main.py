import random


def elige_palabra():
    palabras = ["manzana", "banana", "naranja", "mandarina", "uva", "guitarra", "bajo", "bateria", "trompeta", "violin"]
    return random.choice(palabras)


def muestra_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

   




def juego():
    palabra = elige_palabra()
    letras_adivinadas = []
    intentos = 6
    
    print("Bienvenidx al juego del ahorcado, wachinx!")
    
    while intentos > 0:
        print(muestra_tablero(palabra, letras_adivinadas))
        letra_usuario = input("Introduce una letra, porfis: ").lower()
        
        if letra_usuario in letras_adivinadas:
            print("Ya dijiste esa palabra, elegí otra porfa.")
            continue
        
        letras_adivinadas.append(letra_usuario)
        
        if letra_usuario not in palabra:
            intentos -= 1
            print(f"Nop, incorrecto. Te quedan {intentos} intentos.")
        else:
            print("¡Correcto!")
            
        if set(palabra) <= set(letras_adivinadas):
            print(f"vamooooo, felicidades, ganaste, capx,la palabra era '{palabra}'.")
            return
        
    print(f"Perdiste, ameo, game over. La palabra era '{palabra}'.")

# Arranque del juego
if __name__ == "__main__":
    juego()