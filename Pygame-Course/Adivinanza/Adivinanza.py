#Juego de adivinar un numero
import random
#Variables
intentos = 0;
#Saludo personalizado
print("Hola, ¿como te llamas?")
nombre = input()
print("Muy bien, "+nombre+", he pensado un numero entre 1 y 100, A ver si lo adivinas")
#Generamos un numero aleatorio
numero = random.randint(1,100)
#Inicio del bucle
while intentos < 10:
	numero_adivinar = ''
	numero_adivinar = input()
	numero_adivinar = int(numero_adivinar)
	intentos = intentos + 1

	if numero_adivinar < numero:
		print("El numero que he pensado es MAYOR")
	if numero_adivinar > numero:
		print("El numero que he pensado es MENOR")
	if numero_adivinar == numero:
		print("Bien hecho, haz adivinado el numero que pense!!")
		print("Haz acertado en "+str(intentos)+" intentos")
		break;
if intentos >= 10:
	print("Lo siento no haz acertado, el numero que pense era "+str(numero))