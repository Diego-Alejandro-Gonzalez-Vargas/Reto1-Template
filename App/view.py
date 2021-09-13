"""
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
    ordenado = sa.sort(catalog['Artists'],cmpFunctionRuno)
    indexmin = binary_search_max(ordenado, minimo)
    indexmax = binary_search_max(ordenado, maximo)
    n= indexmax - indexmin
    print("El total de artistas encontrados es: " + str(n))
    x = PrettyTable()
    x.field_names = (["ConstituentID","DisplayName","BeginDate","Nationality","Gender","ArtistBio","Wiki QID","ULAN"])
    x.max_width = 25
    x.hrules=ALL

    for i in range(indexmax-2, indexmax+1):
        artista = lt.getElement(ordenado, i)
        
        x.add_row([artista["ConstituentID"], artista["DisplayName"], artista["BeginDate"],
                   artista["Nationality"], artista["Gender"], artista["ArtistBio"], 
                   artista["Wiki QID"], artista["ULAN"]])
    for i in range(indexmin, indexmin+3):
        artista = lt.getElement(ordenado, i)
        
        x.add_row([artista["ConstituentID"], artista["DisplayName"], artista["BeginDate"],
                   artista["Nationality"], artista["Gender"], artista["ArtistBio"], 
                   artista["Wiki QID"], artista["ULAN"]])




def binary_search_max(arr, x):
    """
    CODIGO SACADO DE: https://www.geeksforgeeks.org/python-program-for-binary-search/
    """
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if lt.getElement(arr, mid)["BeginDate"] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif lt.getElement(arr, mid)["BeginDate"] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return mid


def cmpFunctionRuno(anouno, anodos):
    return (float(anouno["BeginDate"]) < float(anodos["BeginDate"]))

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



    elif int(inputs[0]) == 2:
        minimo=input(print("Año Inicial:\n"))
        maximo=input(print("Año Final:\n"))
        funcionReqUno(catalog, minimo, maximo)

    else:
        sys.exit(0)
sys.exit(0)
