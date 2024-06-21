[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15303646&assignment_repo_type=AssignmentRepo)
# 2do PARCIAL - Algoritmos y Estructuras de datos - 2023

## Modalidad:

Debido a los problemas que esta generando el uso del módulo Safe Exam Browser, no lo utilizaremos en esta instancia de examen. Serán los alumnos/as los responsables de manejar el uso del tiempo provisto. 

- El parcial estará habilitado para su resolución desde: Martes 04/07 @ 18:30hs, hasta: Miercoles 05/07 @ 23:45hs. (pueden elegir cuando comenzar el intento)

- Tienen 1 (uno) sólo  intento para resolver la actividad; el tiempo máximo es 4 (cuatro) horas.

- **El tiempo será contabilizado desde el momento que aceptan realizar la actividad en Github Classroom, y cualquier "commit" realizado luego de 4 horas no será aceptado como parte del intento de resolución!!**

- Los resultados sólo será visibles luego de la fecha límite del Miercoles.   


# Ejercicios:

## Ejercicio 1:

## 1.1: 

Crear una clase <code>Usuario</code>, está contendrá los datos básicos de una persona: nombre, dirección, teléfono, email y fecha de nacimiento, además de los métodos necesarios para cambiar estos datos. Además el usuario tendrá un método especial para "recibir mensajes".

## 1.2:

Crear una clase <code>Libro</code>, está contendrá los datos referentes al libro: nombre, edición, fecha de publicación, y sinopsis, además de los métodos necesarios para cambiar estos datos.  

## Ejercicio 2:

### 2.1:

Modelar una clase <code>Biblioteca</code>; la misma tiene como variables un nombre, una dirección, un teléfono, un email y los horarios de atención de la misma. Ademas de estos datos básicos, la biblioteca debe contener una lista de los libros disponibles. La biblioteca debera proveer métodos para: ingresar nuevos usuarios, prestar libros y aceptar devoluciones de los mismos.

### 2.2: 

Agregar a la clase <code>Biblioteca</code> una lista de los usuarios, la lista deberá contener como información adicional la lista de los libros que el usuario tiene en su posesión. Las listas deben ser representadas utilizando un **Lista Enlazadas**.    

*Nota: los usuarios y libros son del tipo declarado en el Ejercicio 1* 

### 2.3: 

Agregar a la clase <code>Biblioteca</code> una lista enlazada que contenga los libros que han sido prestados, la lista deberá estar ordenada de forma ascendente según la fecha de vencimineto del prestamo, es decir, aquellos libros que el prestamo expira pronto van primero. Si se detectan libros con periodo de prestamo expirados se deberá enviar un mensaje al usuario.    

*Nota: el tiempo de un prestamo es de 30 dias*

### 2.4 

Genrar los **Iteradores** correspondientes para recorrer:
- La lista de usuarios;
- La lista de libros que cada ususrio tiene en su posesion;
- Los libros prestados.


### 2.5

Agrega un método que cree una carpeta llamada "inventario", y que dentro de ella guarde en distintos archivos la lista libros disponibles y los libros prestados. 

*Nota: los archivos pueden ser de texto o binarios*

### 2.6 

Agrega en el <code>\_\_init\_\_</code> de la clase, si los archivos existen, se carguen las listas de libros.

*Nota: los archivos pueden ser de texto o binarios*


## (2 puntos) Ejercicio 3: 

Crear métodos que nos permitan abrir los archivos creados en el Ejercicio 2 y añadir o quitar elementos. 


