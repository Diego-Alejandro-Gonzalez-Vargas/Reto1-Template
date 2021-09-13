"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


def newCatalogA():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None,}

    catalog['Artists'] = lt.newList('ARRAY_LIST')
    catalog['Artworks'] = lt.newList('ARRAY_LIST')


    return catalog

def newCatalogS():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None,}

    catalog['Artists'] = lt.newList('ARRAY_LIST')
    catalog['Artworks'] = lt.newList('ARRAY_LIST')


    return catalog
# Funciones para agregar informacion al catalogo

def addArtists(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['Artists'], artist)
    # Se obtienen los autores del libro
    # ID = artist['Constituent ID']
    
def addArtworks(catalog, artwork):
    # Se adiciona el libro a la lista de libros
    obra = {
        'ObjectID':artwork['ObjectID'],
        'ConstituentID':artwork['ConstituentID'],
        'Title':artwork['Title'],
        'Medium':artwork['Medium'],
        'Dimensions':artwork['Dimensions'],
        'CreditLine':artwork['CreditLine'],
        'DateAcquired':artwork['DateAcquired'],
        'Department':artwork['Department'],
        'URL':artwork['URL'],
        'Height (cm)':artwork['Height (cm)'],
        'Length (cm)':artwork['Length (cm)'],
        'Weight (kg)':artwork['Weight (kg)'],
        'Width (cm)':artwork['Width (cm)']
    }
    lt.addLast(catalog['Artworks'], obra)

    # Se obtienen los autores del libro
    # ID = artist['Constituent ID']
