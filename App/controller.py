﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initdicci(tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    diccio = model.newdicc(tipo)
    return diccio

# Funciones para la carga de datos

def loadData(diccio):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(diccio)
 

def loadVideos(diccio):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videofile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videofile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(diccio, video)
   

# Funciones de consulta sobre el catálogo

def loadaddcategoria(diccio):
    agustinjulio=model.addCategoria(diccio)
    return agustinjulio


def loadvideosLikes(diccio,numero,categor):

    omarperez=model.videosLikes(diccio,numero,categor)

    return omarperez

