import random
import datetime
import json
import os


#
#  1 - GRANULARIDAD Y REUSABILIDAD DE FUNCIONES
#
#  FUNDAMENTAL PARA NO DESAPROBAR QUE NO SE ROMPA EL PROGRAMA
#
#  2 - TRABAJAR LAS VALIDACIONES DE DATO CORRECTO
#

def generar_lista_de_csv (ruta:str)->list:
    
    lista_final = []
    #abre el archivo
    with open (ruta, 'r', encoding='utf-8') as archivo:
        data_cruda = archivo.read()
    #lineas guarda una lista de strings separados por el salto de linea    
        lineas = data_cruda.split("\n")
    #declara la lista que va a devolver por retorno
    #itera 
        for linea in lineas:
            #dato_individual guarda una lista con los valores del string de esa iteracion
            # separados por comas, aun sin clave
            dato_individual = linea.split(',')
            #aca asigno a cada uno de esos valores una variable con el nombre de su futura clave
            id = dato_individual[0]
            nombre = dato_individual[1]
            raza = dato_individual[2]
            poder_de_pelea = dato_individual[3]
            poder_de_ataque = dato_individual[4]
            habilidades = dato_individual[5]

            ###### FUNCIONALIZAR DIVISIOIN DE STRINGS CON GUIONES
            razas = []
            if raza == 'Androide-Humano':
                razas.append('Androide')
                razas.append('Humano')
            elif raza == 'Saiyan-Humano':
                razas.append('Saiyan')
                razas.append('Humano')
            else:
                razas.append(raza)

            habilidades_lista = separar_valores(habilidades, '|$%')

            diccionario = {'id':int(id),
                        'nombre': nombre,
                        'raza': razas,
                        'poder de pelea': int(poder_de_pelea),
                        'poder de ataque': int(poder_de_ataque),
                        'habilidades': habilidades_lista}
            
            lista_final.append(diccionario)
        
        return lista_final

# 1 - Funciones secundarias

def separar_valores (lista, str_separacion:str):
            lista_valores = []
            valores_individuales = lista.split(str_separacion)
            for valor in valores_individuales:
                lista_valores.append(valor.strip())


# 2 Secundarias - listar_razas_unicas

def listar_valores(lista:list, clave:str)->set:
    lista_valores = []
    for elemento in lista:
        lista_momento = elemento[clave]
        for elemento in lista_momento:
            lista_valores.append(elemento)
    
    lista_filtrarda = set(lista_valores)
    return lista_filtrarda

# 2 Principal - Listar cantidad por raza

def listar_cantidad_por_raza(lista:list)->None:
    lista_atributos = listar_valores(lista, 'raza')

    for item in lista_atributos:
        contador = 0
        print('\n-------------------------')
        for heroe in lista:
            lista_momento_1 = heroe['raza']
            for elemento in lista_momento_1:
                if item == elemento:
                    contador += 1
        print(f'Hay {contador} personajes de raza {item}\n') #funcionalizar la impresion

def imprimir_string_y_valor(cadena:str, valor:int):
    print(f"{cadena}")
# 3 Principal

def listar_por_raza(lista:list, clave:str)->None:
    
    lista_atributos = listar_valores(lista, 'raza')
    
    for item in lista_atributos:
        #imprimo cada raza
        print('\n----------')
        print(f'{item}\n')
        for heroe in lista:
            lista_momento_2 = heroe[clave]
            for elemento in lista_momento_2:
                if item == elemento:
                    print(heroe['nombre'])

# 4 - Secundaria - Calcular promedio
def calcular_promedio(a:int, b:int)->int:
    promedio = (a+b)/2
    return promedio

# 4 - Principal - Listar personajes por habilidad: deberá mostrar nombre, raza y promedio de poder entre ataque y defensa
def listar_por_habilidades(lista:list) -> None:
    lista_atributos = listar_valores(lista, 'habilidades')
    
    valor = pedir_dato('habilidad')

    for item in lista_atributos: 
        #imprimo el item de la iteracion actual
        print('\n----------')
        print(f'{item}\n')
        for heroe in lista: #mientras estoy en el item acutal, itero cada personaje de la lista que entra a la funcion por parametro
            lista_momento_2 = heroe['habilidades'] # sabiendo que en esa key hay una lista, la guardo para iterarla
            for elemento2 in lista_momento_2: #itero los valores de lista_momento2
                if item == elemento2: #si el item (recordemos que por ahora estoy en una iteracion de un item prncipal) es igual a uno de los elementos de la lista_momento_2 informo el nombre
                    for raza in heroe['raza']:
                        promedio = calcular_promedio(heroe['poder de pelea'],heroe['poder de ataque'])
                        print(f"Nombre: {heroe['nombre']} - Raza: {raza} - Promedio de poder: {promedio}")
                        #puedo traer la lista de personajes filtrados por raza

# 5 - Jugar batalla

def pedir_dato(dato_a_pedir:str):
    dato = input(f'Ingrese {dato_a_pedir}: ')
    return dato
'''
Acá no tengo que hacer un input sino listar los personajes y matchear id con un input posterior.
Devolver "el personaje elegido es X"
'''
def imprimir_personajes_por_parametro(lista:list, clave1:str, clave2:str)->str:
    for personaje in lista:
        print(f"{personaje[clave1]} - {personaje[clave2]}")

def jugar_batalla(lista:list):

    imprimir_personajes_por_parametro(lista,'id','nombre')

    seleccion = int(input('Selecciona un personaje: '))
    #hacer un while para que no haya una eleccion fuera de rango

    personaje_seleccionado = {}
    personaje_random = random.choice(lista)
    for personaje in lista:
        if seleccion == personaje['id']:
            #print(f"Personaje seleccionado: {personaje['nombre']} | Poder de ataque {personaje['poder de ataque']}")
            personaje_seleccionado = personaje

    print(f"Elegiste a {personaje_seleccionado['nombre']} | Poder de Ataque: {personaje_seleccionado['poder de ataque']}")
    print(f"El sistema ha elegido a {personaje_random['nombre']} | Poder de Ataque: {personaje_random['poder de ataque']}")

    # batalla propiamente dicha
    fecha = datetime.datetime.now()
    if personaje_seleccionado['poder de ataque'] > personaje_random['poder de ataque']:
        print('GANASTE!!')
        print(f"{personaje_seleccionado['nombre']} ha ganado la batalla")
        archivo = open("resultado.txt","a")
        archivo.write(f"{personaje_seleccionado['nombre']} ha ganado la batalla")
        archivo.write(f"{personaje_random['nombre']} es el perdedor.")
        archivo.write(f"Esta batalla se ha dado en la fecha {fecha}")
        archivo.write("---------------------------------------------------------")
        archivo.close() #DESARROLLAR LA FUNCION ESCRIBIR ARCHIVO
    elif personaje_random['poder de ataque'] > personaje_seleccionado['poder de ataque']:
        print('PERDISTE!!')
        print(f"{personaje_random['nombre']} ha ganado la batalla")
    elif personaje_random['poder de ataque'] == personaje_seleccionado['poder de ataque']:
        print(f"Ha habido un empate.")

# 6 - Guardar JSON

def guardar_json(lista:list)->str:
    habilidad_param = input('Ingresa una habilidad: ')
    raza_param = input('Ingresa la raza: ')
    #el ejercicio dice que el usuario ingresa los parametros.
    data_dic = {}
    data_dic['resultados'] = []
    for personaje in lista:
        raza_iterable = personaje['raza']
        habilidad_iterable = personaje['habilidades']

        for raza in raza_iterable:
            if raza == raza_param:
                if habilidad_param in habilidad_iterable:

                    #quito el valor buscado para dejar los restantes en el json
                    #puedo poner un if en caso de haber una sola habilidad
                    habilidad_iterable.remove(f"{habilidad_param}") #esto es lo que le cargo a data_dic
                    data_dic['resultados'].append({
                        "nombre": personaje['nombre'],
                        "poder de ataque": personaje['poder de ataque'],
                        "habilidades": habilidad_iterable
                    })
                    
                    #acá nombro el archivo ↓↓
                    raza_guiones = raza_param.replace(" ","-")
                    habilidad_guiones = habilidad_param.replace(" ","-")
                    nombre_json = f"{raza_guiones}-{habilidad_guiones}.json"

                    with open(nombre_json,"w") as archivo:
                        json.dump(data_dic,archivo,indent=4)
    return nombre_json

def leer_json(nombre_archivo:str):
    #ruta = os.path.dirname(__file__)

    with open(nombre_archivo, "r") as archivo:
        leer = json.load(archivo)
        print(leer)