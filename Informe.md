# Base de Datos 2 - Proyecto 3
### Integrantes
- Anthony Guimarey Saavedra
- Massimo Imparato Conetta
- Sebastian Knell Noriega

## Índice
  - [Introducción](#introducción)
  - [Implementación](#implementación)
    - [Construcción del índice Rtree](#construcción-del-índice-rtree)
    - [Algoritmo de búsqueda KNN](#algoritmo-de-búsqueda-knn)
    - [Algoritmo de búsqueda por Rango](#algoritmo-de-búsqueda-por-rango)
    - [Análisis y experimentación](#análisis-y-experimentación)
    - [Aplicación Web](#aplicación-web)
  - [Prueba de uso](#prueba-de-uso)
  - [Anexos](#anexos)


## Introducción
El objetivo de este proyecto fue implementar un servicio web para la identificación automática de personas a partir de una colección grande de imágenes de rostros. 
Esta enfocado en la construcción optima de una estructura multidimensional para dar soporte a las búsquedas y recuperación eficiente de imágenes. Para ello hacemos uso de la libreria [Face Recognition](https://github.com/ageitgey/face_recognition). En dicha librería ya se encuentra implementado las técnicas necesarias para obtener de cada imagen una representación numérica y compacta (enconding). Se usará una colección de referencia con más de 13 mil imágenes de rostros de personas, disponible en el [siguiente enlace](http://vis-www.cs.umass.edu/lfw/).


## Implementación
### Construcción del índice Rtree
Para construir el índice Rtree ...


### Algoritmo de búsqueda KNN



### Algoritmo de búsqueda por Rango



### Análisis y experimentación

Tiempo | KNN-Rtree | KNN-Secuencial
------------ | ------------- | -------------
N=100 | aaa | aaa
N=200 | aaa | aaa
N=400 | aaa | aaa
N=800 | aaa | aaa
N=1600 | aaa | aaa
N=3200 | aaa | aaa
N=6400 | aaa | aaa
N=12800 | aaa | aaa

Valor de K = 8

### Aplicación web
Para visualizar los resultados implementamos una pequeña aplicación web usando [Flask](https://flask.palletsprojects.com/en/2.0.x/#) para el servidor y [Angular](https://angular.io/) para el front. A continuación se muestra la interfaz.


## Prueba de uso
Se adjunta el siguiente video que muestra la funcionalidad de la aplicación.

[DB2 - Proyecto 3 - Funcionalidad de la aplicación](https://drive.google.com/file/d/1uTbBVfxx8i-gB0EQekEFLWN_Aag8p-hA/view)

## Anexos
