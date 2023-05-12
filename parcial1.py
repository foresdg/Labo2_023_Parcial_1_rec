from os import system
#import csv
from funciones_Agustin_Forestieri_v3 import *

system('cls')

while True:

    respuesta = (input("""\n\n
                        ╔══════════════════════════════════════════════════╗
                        ║                 P A R C I A L   I                ║
                        ╚══════════════════════════════════════════════════╝
                        \n
                        1 - Traer datos desde archivo
                        2 - Listar cantidad por raza
                        3 - Listar personajes por raza
                        4 - Listar personajes por habilidad
                        5 - Jugar batalla
                        6 - Guardar JSON
                        7 - Leer JSON
                        8 - Salir del programa >>\n
                        Elija una opcion (minuscula): """))
    

    respuestas = ['1','2','3','4','5','6','7','8']
    #if respuesta == '1' and bandera_opcion_uno == True:
    
    if respuesta in respuestas:
        
        bandera_opc_uno = True
        bandera_opc_seis = True

        match respuesta:
            case '1':
                bandera_opc_uno = False
                lista = generar_lista_de_csv('Parcial2023.\DBZ.csv')
                if lista != None:
                    print('\nDatos importados correctamente.')
                #print(lista)
                # 1 - Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
                #     cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
                #     un personaje puede tener más de una raza y más de una habilidad.
                pass
            case '2':
                if bandera_opc_uno == True:
                    print('\nPor favor, cargue la lista en OPCION 1 para usar esta función\n')
                    pass
                else:    
                    listar_cantidad_por_raza(lista)
                    pass
                # 2 - Listar cantidad por raza: mostrará todas las razas indicando la cantidad 
                # de personajes que corresponden a esa raza.
            case '3':
                if bandera_opc_uno == True:
                    print('\nPor favor, cargue la lista en OPCION 1 para usar esta función\n')
                    pass
                else:    
                    listar_por_raza(lista, 'raza')
                    pass
                
                # 3 - Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
                #     personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
                #     repetirse en los distintos listados.
            case '4':
                if bandera_opc_uno == True:
                    print('\nPor favor, cargue la lista en OPCION 1 para usar esta función\n')
                    pass
                else:
                    listar_por_habilidades(lista,'raza')
                    pass
                # 4 - Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad 
                #     y el programa deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.
            case '5':
                if bandera_opc_uno == True:
                    print('\nPor favor, cargue la lista en OPCION 1 para usar esta función\n')
                    pass
                else:
                    jugar_batalla(lista)
                    pass
                # 5 - Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. 
                #     Gana la batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla 
                #     se deberá guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del 
                #     personaje que ganó y el nombre del perdedor. Este archivo anexará cada dato.

            case '6':
                if bandera_opc_uno == True:
                    print('\nPor favor, cargue la lista en OPCION 1 para usar esta función\n')
                    pass
                else:
                    guardado = guardar_json(lista)
                    bandera_opc_seis == True
                    pass
                # 6 - Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes 
                #     que cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
                #     guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
                #     búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
                #     Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
                #     Nombre del archivo:
                #     Saiyan_Genki_Dama.Json
                #     Datos :
                #     Goten - 3000 - Kamehameha + Tambor del trueno
                #     Goku - 5000000 - Kamehameha + Super Saiyan 2
            case '7':
                # 7 - Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json 
                #     de la opción 6.
                if bandera_opc_seis == True and bandera_opc_uno == True:
                    print('\nPor favor, cargue la lista en OPCION 1 para usar esta función\n')
                    pass
                else:
                    leer_json(guardado)
                    pass
            case '8':
                # H - Informar altura promedio del genero F
                print('\n\nGracias por utilizar nuestro sistema\n\n')
                break
    
    elif respuesta not in respuestas:
        print(f"\n{respuesta} no es una opción válida.\nIngresa un valor de 1 a 8")
        pass