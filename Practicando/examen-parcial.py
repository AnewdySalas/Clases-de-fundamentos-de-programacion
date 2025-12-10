
print("="*30)
print("¿Podras adivinar el numero?")
print("="*30)
import random

resultado = random.randint(1, 10)
 
intento = 3


while intento > 0:
    

    intenta = int(input("Ingresa un numero del 1 al 10: "))

    if intenta > 10 or intenta < 0:
        print("Ingresa un numero valido")
        continue
    
    if  intenta == resultado:
        print("Ganaste eres el mejor!!")
        print("Gracias por jugar")
        exit(0)
    
    elif intenta > resultado:
        print(f"El numero es menor que {intenta}, intenta de nuevo.")
    
    elif intenta < resultado:
        print(f"El numero es mayor que {intenta}, intenta de nuevo")

    intento -= 1

    if intento == 0:
        print(f"Perdiste todas tus intentos. El numero era {resultado}.")
        break
   
    
    
    


    


