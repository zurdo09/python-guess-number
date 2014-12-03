#-*- coding: utf-8 -*-
import random
import time
import sys
#Bienvenida
print " "
print "\t\t\t\t....................................................................."
print "\t\t\t\t............................BIENVENDIDO A............................"
print "\t\t\t\t........................¡Adivina un Número!!!........................"
print "\t\t\t\t....................................................................."
print " "
print " "
#Instrucciones del Juego
print "El objetivo del juego es el siguiente:"
print " "
print "--- El sistema generará automaticamente números al azar, del cual, tendras que ingresar un número entero entre los rangos 0 y 10 para adivinar el que el sistema genera, además tienes que tener en cuenta que si ingresas un caracter tipo string perderas el turno por no seguir instrucciones---"
print " "
print "Bueno. Pues a ¡Jugar se ha dicho!"
# Las Instrucciones son importantes para que el usuario sepa que hacer y no olvidar imprimirlas con print
print " "
print "¿Estás listo?"
print " "
listo = True
while listo==True:
	print "Ingresa 'y' si lo estás y 'n' si no lo estás."
	preg = raw_input("Escribe 'y' o 'n':   ")
	print " " 
    #Nuestro contador de intentos
	contador = 1 
	#Número aleatorio por el sistema
	num_aleatorio = random.randint(0,10) 
	#Convierte los caracteres a minúsculas.
	if preg.lower()=="y":
		print "Ok. Cuentas con 5 intentos. ¡No los Desperdicies!"
		print " "
		#Cuenta 5 turnos para el jugador o usuario.
		while contador < 6:
			try:
				print ("Numero de Intento: " + str(contador))
				contador = contador + 1
                # No olvidar imprimir el contador para saber el numero de intentos 
				pov=True
				while pov==True:
					numero = raw_input("Elige un número del 1 al 10: ")
					numero = int(numero)
					if numero >=0 and numero <=10:
						print " "
						print "Procesando..."
						print " "
						time.sleep(2) 
						if numero < num_aleatorio:
							print ("→→→ Tu número es mas bajo que el generado por el sistema." )
							print "Intentalo de nuevo"
							print " "
							break
						if numero > num_aleatorio:
							print ("→→→ Tu número es mas alto que el generado por el sistema." )
							print " "
							break
					else:
						pov == False
						print "Número fuera de rango. Intente de nuevo."
						print " "
			except ValueError,NameError:
                	# el except sirve para que no nos saque del programa y el usuario siga solo que corrija su error  
						print "***Error Solo se pueden Ingresar Números. Perdiste el turno***"
						print " "	
		#Condicion igualitaria al numero aleatorio.								
		if numero == num_aleatorio: 
			print ("¡WoW Eres un genio....!")
			print " "
			print ( " lo lograste con %d intentos" % (contador))
			break
			# se puede usar modulo o suma para concatenar
			break
		#Condicion diferente de "final del juego"	
		if numero != num_aleatorio:
			print ("Has perdido. xS será en otra ocasión.")
			print "Saliedo....."
			break
			sys.exit(1)
	elif preg.lower()=="n":
		listo == False
	else:
		print "No es una respuesta correcta. ¡Intentalo de Nuevo!"
