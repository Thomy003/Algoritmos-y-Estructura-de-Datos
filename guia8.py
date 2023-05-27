#--------------------------------------------------- ejercicio 1 ---------------------------------------------------#

#a)
def pertenece(s: 'list[int]', e: int) -> bool:
    return e in s
''' es un string largo
print(pertenece([1,2,3,4,5,6,7,8], 6))
'''

#b)
def divideATodos(s: 'list[int]', e: int) -> bool:
    lista_copiada: list
    lista_copiada = s.copy() #creo una variable nueva que funciona como lista pero no modifica los elementos de la lista original s

    while len(lista_copiada) > 0 and lista_copiada[-1] % e == 0:
        lista_copiada.pop()
        pass #built in que me evita que se rompa el codigo
    
    if(len(lista_copiada) > 0):
        return False
    else:
        return True
    
#print(divideATodos([6,12,18], 6))
#print(divideATodos([], 6))

'''
for i in s: #Este for recorre todos los elementos de la lista

for i in range(0,len(s),1): #Este for comienza desde el numero 0 hasta la lomgitud de la lista pero no toma los elementos de la lista en si
    s[i] #aca es cuando tomo al elemento con cierto indice de la lista

s[i:j] = t
 esta me genera como una sublista que coomienza desde el indice i hasta el indice j
'''

#c)
def sumaTotal(s: 'list[int]') -> int:
    res: int = 0
    for i in s:
        res = res + i
    return res
    
#print(sumaTotal([6,12,18]))
#print(sumaTotal([]))


#d)
def ordenados(s: 'list[int]') -> bool:
    for i in range(1,len(s)-1):
        if(s[i] < s[i+1]):
            pass
        else:
            return False
    return True

#print(ordenados([1,2,3]))
#print(ordenados([1,4,2,3]))
#print(ordenados([])) en caso de que este vacia como se ejecuta el codigo osea el for como funciona con la lista vacia?

#e)
def palabraLarga(s: 'list[str]') -> bool:
    for i in s:
         if len(i) >= 7:
             return True
    return False

#print(palabraLarga(['holaaaa','como','estassasadss']))
#print(palabraLarga(['hola','como','estas']))
#print(palabraLarga([]))

#f)
def es_palindroma(palabra: str) -> bool:
    valor: bool
    valor = True

    while len(palabra) > 1 and valor == True:
        if(palabra[0] == palabra[-1]):
            palabra = palabra[1:-1]
        else:
            valor = False

    return valor
#print(es_palindroma('olalo'))
#print(es_palindroma('ThomyymohT'))
#print(es_palindroma('Thomyymoht'))
#print(es_palindroma(' '))
#print(es_palindroma('abcdeba'))

#g)
def secure_password(password: str) -> str:
    lowercase: bool = False
    uppercase: bool = False
    number: bool = False

    for i in range(0,len(password),1):
            if str.islower(password[i]):  #puedo escribirlo como str.islower(password[i]) o password[i].islower() CUAL ES MEJOR?
                lowercase = True
            if password[i].isupper():
                uppercase = True
            if str.isnumeric(password[i]):
                number = True
    
    if len(password) < 5 :
        print("Rojo")
    elif len(password) > 8 and lowercase and uppercase and number:
        print("Verde")
    else:
        print("Amarillo")
        
#secure_password('miCOnTra1234')
#secure_password('MICONTRA1234')
#secure_password('micontra1234')
#secure_password('miContraesLARga')
#secure_password('m1Ca')


#h)
moneyInBank: int = 0 
def bankAccountMovements(account: 'list[(int, str)]') -> tuple: 
    global moneyInBank #La varible global se define solo una vez dentro de la funcion
    for transaction in account:
        if 'I' in transaction: #Puedo llamar a la funcion in que se fija si el elemento pertenece a la tupla
            moneyInBank = moneyInBank + transaction[0]
        elif transaction[1] == 'R':
            moneyInBank = moneyInBank - transaction[0]
        else:
            pass
    return print("Saldo:" , moneyInBank)
    
#bankAccountMovements([(200,'I'), (2000,'I'), (500,'R'), (200,'I')])
#bankAccountMovements([(200,'R'), (2000,'I'), (500,'R'), (5000,'R')])

#i)
def different_vowels(word: str) -> bool:
    vowels: int = 0
    if 'a' in word:
        vowels = vowels + 1 #si en vez de poner vowels = vowels + 1 reemplazo a todos por vowels =+ 1 nunca suma mas de 1
        
    if 'e' in word:
        vowels = vowels + 1
        
    if 'i' in word:
        vowels = vowels + 1
        
    if 'o' in word:
        vowels = vowels + 1
        
    if 'u' in word:
        vowels = vowels + 1

    if vowels > 2:
        return True
    else:
        return False
    
vocales: list = ['a','e','i','o','u']

def different_vowels_shortcut(word: str) -> bool:
    global vocales
    lista_vocales: list = vocales.copy()

    for letter in range(len(word)):    #
        if word[letter] in lista_vocales:
            for vowel in lista_vocales:
                if word[letter] == vowel:
                    lista_vocales.remove(vowel) #la funcion lista.remove(x) me devuelve una lista sin el elemento x 

    if len(lista_vocales) > 2:
        return False
    else:
        return True

''' por que esto tira error?
    for letter in range(len(word)):    
        if word[letter] in lista_vocales:
            for vowel in range(len(lista_vocales)):
                if word[letter] == listavocales[vowel]:
                    lista_vocales.pop(listavocales[vowel])
'''


#print(different_vowels_shortcut('afdaehi'))
#print(different_vowels_shortcut('afdahi'))
    
#print(different_vowels('hola'))
#print(different_vowels('hoolaaa'))
#print(different_vowels('hola como estas'))


#--------------------------------------------------- ejercicio 2 ---------------------------------------------------#

#1)
def amongzeros(lista: list) -> list:
    for i in range(0,len(lista),1):
        if i % 2 == 0:
            lista[i] = 0
        else:
            pass
    return lista

#print(amongzeros([2,5,1,9,3,8]))
#print(amongzeros([2,5,1,9,3,8,4]))


#2)
def amongzeros_sin_modificar_lista_original(lista: list) -> list:
    lista_no_original: list = lista.copy()
    for i in range(0,len(lista_no_original),1):
        if i % 2 == 0:
            lista_no_original[i] = 0
        else:
            pass
    return lista_no_original

lista: list = [2,5,1,9,3,8]
#print(amongzeros_sin_modificar_lista_original(lista))
#print(lista)

#3)
def word_without_vowels(word: str) -> str: #en esta funcion la varaible word que se modifica se pasa por value y no reference, por eso cuando llame a word fuera de la funcion va a tomar su valor global y no el local dentro de esta funcion
    lista: 'list[str]' = []
    for letter in range(0,len(word)):
        if word[letter] in vocales:
            pass
        else:
            lista.append(word[letter])
    
    word = ''.join(lista)   #Esta funcion me permite concatenar los elementos de una lista usando un parametro '' en este caso solo concatena los elementos sin modificarlos, por ejemplo si pusiera ' ' cuando llame a la funcion en vez de devolverme "hl" me devolveria "h l"
    return word

word: str = 'holaa'
#print(word_without_vowels(word))
#print(word)


#4)
def reemplazaVocales(word: str) -> str:
    for letter in range(0,len(word)):
        if word[letter] in vocales:
            word = word.replace(word[letter],'-') #debo poner word = word.replace(x,y) porque sino no se sobreescribe la palabra. x es el parametro que quiero cambiar e y es el parametro al cual quiero que se cambie.
        else:
            pass
    return word

#print(reemplazaVocales(word))
#print(word)

#5)
def daVueltaStr(word: str) -> str:
    lista: list = []
    for letter in range(len(word)-1, -1, -1): #range empieza con el lenght de la lista menos uno porque para jola len = 4, pero su ultimo elemento tiene como posicion el indice 3.
        lista.append(word[letter])
    return ''.join(lista)

#print(daVueltaStr('jola'))




#--------------------------------------------------- ejercicio 3 ---------------------------------------------------#

#1)
name_list: list = []
def students_names(name: str) -> list:
    name_list.append(name)

print("Escriba un nombre: ")
name: str = input()
while name != "listo":
    students_names(name)
    print("Escriba un nombre: ")
    name: str = input()

print(name_list)


#2)
monedero_electronico: int = 0
historial: 'list[tuple]' = []
def historial_monedero_electronico(operacion: str, cash: int) -> 'list[tuple]':
    global monedero_electronico
    if operacion == "C":
        monedero_electronico = monedero_electronico + cash
    else:
        monedero_electronico = monedero_electronico - cash
    historial.append((operacion, monedero_electronico))

print("Que operacion desea realizar (C), (D), (X)")
operacion: str = input()
while operacion != "X":
    print("Ingrese un monto: ")
    cash: int = int(input())      #La funcion input() que me permite interactuar en live con el teclado, solo devuelve comandos de tipo string, por eso lo debo modificar al dato al tipo de dato con el cual quiero trabajar
    historial_monedero_electronico(operacion, cash)
    print("Que operacion desea realizar (C), (D), (X)")
    operacion: str = input()

print(historial)


#3)
import random

def random_number():
    number_list: 'list[int]' = [0,1,2,10,11,12]
    print(random.randint(0,12)) #Imprime un numero aleatorio entre 0 y 12
    print(random.choice(lista)) # imprime un elemento aleatorio que esta dentro de una lista

random_number()



#--------------------------------------------------- ejercicio 4 ---------------------------------------------------#

#1)
def perteneceACadaUno(s: 'list[list]', e: int) -> 'list[bool]':
    new_list: list = []
    if s == []:
        return True
    
    for lista in s:
        if pertenece(lista, e):
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list

#print(perteneceACadaUno([[1],[2,3,5],[2,5],[1,6],[2]], 2))
#print(perteneceACadaUno([[]], 2)) #retorna False
#print(perteneceACadaUno([], 2)) #retorna True debido al implica de la especificacion

#2)
def esMatriz(s: 'list[list]') -> bool:
    if len(s) > 0 and len(s[0]) > 0:
        for list in s:
            if len(list) == len(s[0]):
                pass
            else:
                return False
        return True
    else:
        return False
    
#print(esMatriz([[1,2,3],[4,53,7]]))
#print(esMatriz([[1,2,3],[4]]))
#print(esMatriz([[],[4,53,7]]))
#print(esMatriz([[],[]]))
#print(esMatriz([]))

#3)
def filasOrdenadas(m: 'list[list]') -> 'list[bool]':
    boolean_list: 'list[bool]' = []
    for lista in m:
        if ordenados(lista):
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    return boolean_list

#print(filasOrdenadas([[1,2,3],[3,2,1],[6,4,5],[6,9,19]]))
#print(filasOrdenadas([[1],[3],[6],[6]]))

#4)