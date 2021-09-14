﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.Algorithms.Sorting import shellsort as sa
from time import process_time
from prettytable import PrettyTable, ALL

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposicion en el museo")
    print("8- SALIR")

def printMenuED():
    print("1- Cargar información por ARRAY_LIST")
    print("2- Cargar información por SINGLE-LINKED")
    

def initCatalogA():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalogA()

def initCatalogS():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalogS()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def funcionReqUno(catalog, minimo, maximo):
    ordenado= controller.funcionReqUno(catalog,minimo,maximo)
    print("la cantidad de artistas encontrados es:" +str(lt.size(ordenado)))
    x = PrettyTable()
    x.field_names = (["ConstituentID","DisplayName","BeginDate","Nationality","Gender","ArtistBio","Wiki QID","ULAN"])
    x.max_width = 25
    x.hrules=ALL

    for i in range(1, 4):
        artista = lt.getElement(ordenado, i)
        
        x.add_row([artista["ConstituentID"], artista["DisplayName"], artista["BeginDate"],
                   artista["Nationality"], artista["Gender"], artista["ArtistBio"], 
                   artista["Wiki QID"], artista["ULAN"]])
    for i in range((lt.size(ordenado)-2), lt.size(ordenado)+1):
        artista = lt.getElement(ordenado, i)
        
        x.add_row([artista["ConstituentID"], artista["DisplayName"], artista["BeginDate"],
                   artista["Nationality"], artista["Gender"], artista["ArtistBio"], 
                   artista["Wiki QID"], artista["ULAN"]])
    print(x)

def funcionReqDos(catalog, minimo, maximo):
    lista_f = controller.funcionReqDos(catalog, minimo, maximo)
    size = lt.size(lista_f)
    print("Se encontraron "+str(size)+"obras en ese rango de fechas")
    x = PrettyTable()
    
    x.field_names = (["ObjectID","Title","Artists", "Medium", "Dimensions",
                      "DateAcquired", "URL"])
    x.max_width = 25
    x.hrules=ALL

    if size >= 6:
        for i in range(1, 4):
            artwork = lt.getElement(lista_f, i)
            
            x.add_row([artwork["ObjectID"], artwork["Title"], artwork["Artists"],
                    artwork["Medium"], artwork["Dimensions"], artwork["DateAcquired"], 
                    artwork["URL"]])

        for i in range(size-2, size+1):
            artwork = lt.getElement(lista_f, i)
            x.add_row([artwork["ObjectID"], artwork["Title"], artwork["Artists"],
                    artwork["Medium"], artwork["Dimensions"], artwork["DateAcquired"], 
                    artwork["URL"]])
    
    else:
        for i in range(1,size+1):
            artwork = lt.getElement(lista_f, i)
            x.add_row([artwork["ObjectID"], artwork["Title"], artwork["Artists"],
                        artwork["Medium"], artwork["Dimensions"], artwork["DateAcquired"], 
                        artwork["URL"]])
    print(x)





"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        printMenuED()
        ed = input(print("Cual desea escojer:\n"))
        if int(ed)==1:
            catalog = initCatalogA()
            t1 = process_time()
            loadData(catalog)
            t2 = process_time()
        elif int(ed)==2:
            catalog = initCatalogS()
            t1 = process_time()
            loadData(catalog)
            t2 = process_time()
        print("Cargando información de los archivos ....")
        
        print('Artistas cargados: ' + str(lt.size(catalog['Artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['Artworks'])))
        print("Time = " + str(t2 - t1) + "seg")
        artistas = catalog['Artists']
        for cont in range(1, 4):
            artista = lt.getElement(artistas, lt.size(catalog['Artists'])-cont)
            print(artista)
        obras = catalog['Artworks']
        for cont in range(1, 4):
            obra = lt.getElement(obras, lt.size(catalog['Artworks'])-cont)
            print(obra)
        otra = catalog['Artists_Artworks']
        for cont in range(1, 4):
            obra = lt.getElement(otra, lt.size(catalog['Artists_Artworks'])-cont)
            print(obra)



    elif int(inputs[0]) == 2:
        minimo=input(print("Año Inicial:\n"))
        maximo=input(print("Año Final:\n"))
        funcionReqUno(catalog, minimo, maximo)
    elif int(inputs[0]) == 3:
        minimo=input(print("Fecha Inicial:\n"))
        maximo=input(print("Fecha Final:\n"))
        funcionReqDos(catalog, minimo, maximo)
    else:
        sys.exit(0)
sys.exit(0)
