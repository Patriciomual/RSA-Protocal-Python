#-*- coding:utf-8-*-
#from progress.bar import Bar, ChargingBar  # Para ejecutar estas librerias instalar progress, pero no es relevante en 
#import os, time 							# en la ejecución del código, solo es visual.
import random
import numpy as np

  
def phi(p,q):

	ph = (p-1)*(q-1) 				# Teorema de Euler,aplicado a numeros
					 				# donde se cumple siempre la misma condición
	return ph 

def exp(x,k,n):						# Función de exponenciación modular
									# ocupada para encontrar una expresión congruente
	acumulador = 1					# de un modulo demaciado grande para el computo.
	cont = 0
	while k!= 0:
		if (k%2)==1:
			acumulador = (acumulador*x)%n
		x = (x*x)%n
		k = k/2
		cont = cont +1
	return acumulador

def mcd(a,b):						# Obtenemos el maximo común denominador 
									# necesario para muchas de las funciones posteriores.
	while b != 0:
		a, b = b, a % b
	return a

def Test_Miller_Rabin(n,k):			# Recibo como parametro el numero a verificar N
									# para determinar si es primo o no, función fundamental
    if n % 2 == 0:					# en el protocolo RSA.
        return False

    r, s = 0, n - 1

    while s % 2 == 0:				# Mientras s el cual fue inicializado en 0 tenga
        r += 1						# un modulo igual a 0 se aplicará un ciclo for hasta la cantidad de iteraciones 
        s //= 2						# seleccionadas por el usuario.
    for i in xrange(k):
        a = random.randrange(2, n - 1) 	# Se genera el numero de a de forma random entre 2 y n-1
        x = pow(a, s, n)				# pow hace referencia a trabajar con exponentes, seŕia lo mismo que x**a
        if x == 1 or x == n - 1:		# Condicion donde se determina la continuidad del algoritmo.
            continue
        for i in xrange(r - 1):	
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False			# Para el caso de no ser primo se retorna un Booleano False
    return True						# En caso contrario retorna un Booleano  True

def Inverso(e, phi):				# Esta función determina el valor de d, de gran importancia que hace referencia
									# a la clave privada ocupada para desencriptar.
    d = 0							# Resive como argumentos e y phi para el calculo posterior.
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1						# Retorna el inverso de e (mod phi) equivalente a d.
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def Desencriptacion():
	
	m = exp(c,d,n)%n 	
	return m 						# Se retorna tanto los valores aleatorios de p y q, n el valor de phi y el de la
									# la clave secreta d

def Encriptacion():

	m = input("Mensaje: ")
	global c 
	c = exp(m,e,n)%n 				# Encriptación del mensaje, usando exponenciacion modular , para determinar su valor congruente.
				
#	bar2 = ChargingBar('Codificando:', max=100) 
#		
#	for num in range(100):							# Libreria progress para la animación de carga, solo visual.
#
#		time.sleep(random.uniform(0, 0.05))
#		bar2.next()
	
#	bar2.finish()
	print "\nMensaje codificado:",c

#----------------------------------- main() ---------

global e,n
cont = 0
verifica_0 = []
verifica_1 = [] 	

digitos_p= input("cantidad de digitos P:")  # Cantidad de digitos de numeros aleatorios seleccionados por el usuario
digitos_q= input("cantidad de digitos Q:")	

h = input("iteraciones:")				
var_0 = False
var_1 = False

cont = 0
while var_0 == False : 						# Se generan los valores de forma aleatoria , los que son de inmediato enviados al test
											# Miller-Rabin para verificar su primalidad, esto se realizara hasta cuando exista un numero primo
    p = int(''.join(["%s" % random.randint(1, 10) for num in range(1, digitos_p)]))
    var_0 = Test_Miller_Rabin(p,h)			
    cont += 1

#---------------------------------------------------
while var_1 == False: 						# Misma aolicación de lo anterior, pero para generar el valor de q y revisar su primalidad.
 
    q = int(''.join(["%s" % random.randint(1, 10) for num in range(1, digitos_q)]))
    var_1 = Test_Miller_Rabin(q,h)
    cont += 1
   
#----------------------------------------------

n = p*q 						# Producto n público generado por dos números (p y q)
								# primos testeados con anterioridad.
phi = phi(p,q)					# Llamado a función phi, teoria de Euler


e = random.randrange(1,phi,1)	# Generación de e de forma aleatoria, necesaria para entrar en el ciclo
								# posterior.
while mcd(e,phi) != 1:

								# Generación de variable e tal que mcd(e,phi)=1 y en el intervalo 1 a phi
	e = random.randrange(1,phi,1)

#-----------------------------------------------
d = Inverso(e, phi)       		# Obtenemos la clave secreta para desencriptar
								# mediante su inverso multiplicativo.

print "*******************************"
print "Valores: \n\np:",p,"\n\nq:",q,"\n\nN",n,"\n\nPhi:",phi,"\n\ne:",e,"\n\nd:",d
print "*******************************"

#-----------------------------------------------
Encriptacion()					#Llamado a funcion de encriptacion, donde definiremos el mensaje de forma numerica para encriptar
Des = Desencriptacion()			#Llamado a funcion de Desencriptacion, donde con los valores de el mensaje encriptado, la clave privada y el n(p*q) público
print "\n\nMensaje desencriptado:",Des
