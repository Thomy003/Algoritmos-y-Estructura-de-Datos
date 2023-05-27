#-------------------------- ejercicio 1 --------------------------#
import math

#a)
def raizDe2() -> float:
    resultado : float = round(math.sqrt(2), 4)
    print(resultado) #esto imprime el resultado
    return resultado #esto retorna el resultado

#b)
def imprimir_hola() -> None:   #no devuelve nada
    print('hola')

#c)

def imprimir_un_verso() -> None:
    print("I wanna go \nI wanna go far away \nWhere nobody knows \nMy nameeeeeee")

#d)

def factorial_2() -> int:
    res = math.factorial(2)
    return res

#e)

def factorial_3() -> int:
    res = math.factorial(3)
    return res

#f)

def factorial_4() -> int:
    res = math.factorial(4)
    return res

#g)
def factorial_5() -> int:
    res = math.factorial(5)
    return res

#-------------------------- ejercicio 2 --------------------------#

#a)
def imprimir_saludo(nombre: str):
    #nombre: str  
    #nombre = 'Thomy'                 si pongo esto se va a imprimir siempre Thomy y nunca el nombre que le pase por parametro
    print('Hola '+ nombre)


#b)
def raiz_cuadrada_de(numero: int) -> int:
    return math.sqrt(numero)

#c)
def imprimir_dos_veces(estribillo: str) -> str:
    estribillo = "I wanna go \nI wanna go far away \nWhere nobody knows \nMy nameeeeeee"
    print(estribillo + estribillo) #el + concatena 2 string
    print(estribillo * 2) #el * necesita de un int para concatenarse con si mismo n veces

#d)
def es_multiplo_de(n: int, m: int) -> bool: #si tengo return tengo que marcar que devuelvo un bool?
    while (n >= m):
        n = n - m

    if (n == 0):
        return True
    else:
        return False
    
#e)
def es_par(n: int) -> bool:
    return es_multiplo_de(n,2)

#f)
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    cantidad_de_porciones_totales : int = comensales*min_cant_de_porciones
    cantidad_de_pizzas_totales : int = 0

    while (cantidad_de_porciones_totales > 0):
        cantidad_de_porciones_totales = cantidad_de_porciones_totales - 8
        cantidad_de_pizzas_totales += 1
    
    return cantidad_de_pizzas_totales



#-------------------------- ejercicio 3 --------------------------#

#a)
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

#b)
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

#c)
def es_nombre_largo(nombre: str) -> bool:
    return len(nombre)>=3 and len(nombre)<=8

#d)
def es_bisiesto(anio: int) -> bool:
    return (anio%400 == 0) or ((anio%4 == 0) and (not(anio%100 == 0)))

#-------------------------- ejercicio 4 --------------------------#

#como utilizo las funciones min y max en este ejercicio? lista = [3.1,5,2,4.1,1.8,2.7,2,2.6,4.1,7,1.25]

#a)
def peso_pino(metros_pino: float) -> float:
    centimetros_pino : int = metros_pino * 100
    if (centimetros_pino <= 300):
        return centimetros_pino * 3    
    else:
        return 300 * 3 + (centimetros_pino - 300) * 2
    
#b)
def es_peso_util(peso_pino: float) -> bool:
    if(peso_pino >= 400 and peso_pino <= 1000):
        return True
    else:
        return False

#c) 
def sirve_pino(metros_pino: float) -> bool:
    return es_peso_util(peso_pino(metros_pino)) #Seria esto composicion de funciones?

#-------------------------- ejercicio 5 --------------------------#

#a)
def devolver_el_doble_si_es_par(numero: int) -> int:
    if(numero % 2 == 0):                                # % me devuelve el resto
        return numero*2
    else:
        return numero
    
#b)
def devolver_el_valor_si_es_par_sino_el_que_le_sigue(numero: int) -> int:
    if(numero % 2 == 0):
        return numero
    else:
        return numero + 1

#c) 
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if (numero % 9 == 0):
        return 3*numero
    elif (numero % 3 == 0):
        return 2*numero
    else:
        return numero 
    
#d)
def nombre_largo(nombre: str) -> str:
    if(len(nombre) > 4):
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
#e) 
def anda_a_laburar(sexo: str, edad: int) -> str:
    if (sexo == "F" and (edad > 60 or edad < 19)):
        print("Anda de vacaciones")
    elif (sexo == "M" and (edad > 65 or edad < 19)):
        print("Anda de vacaciones")
    else:
        print("Te toca trabajar")


#-------------------------- ejercicio 6 --------------------------#
#a)
def imprimir_numeros_menores_a10() -> None:
    numero : int = 1
    while(numero < 11):
        print(numero)
        numero += 1

#b)
def imprimir_numeros_pares_entre10y40() -> None:
    numero : int = 10
    while(numero < 41):
        if(numero % 2 == 0):
            print(numero)
        numero += 1

#c)
def imprimir_eco_10veces() -> None:
    repeticion : int = 1
    palabra: str = "eco"
    while(repeticion < 11):
        print(palabra)
        repeticion += 1

#d)
def cuenta_regresiva(numero: int) -> None:
    while(numero > 0):
        print(numero)
        numero = numero - 1
    print("Despegue")

#e)
def viaje_en_el_tiempo(anio_partida: int, anio_llegada: int) -> None:
    while(anio_partida>anio_llegada):
        anio_partida = anio_partida - 1
        print("Viajamos un anio al pasado, estamos en el anio" , anio_partida)

#f)
def viaje_para_conocer_al_aristoteles(anio_partida: int) -> None:
    while(anio_partida > -365):
        anio_partida = anio_partida - 20
        print("Viajamos 20 anios al pasado, estamos en el anio" , anio_partida)

#-------------------------- ejercicio 7 --------------------------#

#a)
def imprimir_numeros_menores_a10_for() -> None:
    for numero in range(1,11):
        print(numero)

#b)
def imprimir_numeros_pares_entre10y40_for() -> None:
    for numero in range(10,41,2):
        print(numero)

#c)
def imprimir_eco_10veces_for() -> None:
    for numero in range(1,11):
        print("eco")

#d)
def cuenta_regresiva_for(numero: int) -> None:
    for regresion in range(numero,0,-1):
        print(regresion)
    print("Despegue")

#e)
def viaje_en_el_tiempo_for(anio_partida: int, anio_llegada: int) -> None:
    for anio in range(anio_partida,anio_llegada - 1, -1):
        print("Viajamos un anio al pasado, estamos en el anio" , anio)

#f)
def viaje_para_conocer_al_aristoteles_for(anio_partida: int) -> None:
    for anio in range(anio_partida, -394, -20):
        print("Viajamos 20 anios al pasado, estamos en el anio" , anio)

#-------------------------- ejercicio 8 --------------------------#

#a)
def a():
    x : int = 5
    y : int = 7
    print(x , y)

#b)
def b():
    x : int = 5
    y : int = 7
    z : int = x + y
    print(z)
    
#c)
def c():
    x : int = 5
    x : str = "hora"
    print(x)

#d)
def d():
    x : bool = True
    y : bool = False
    print(x and y)

#e)
def e():
    x : bool = False
    print(not x)


#-------------------------- ejercicio 9 --------------------------#

#a)
def rt(x: int, g:int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g