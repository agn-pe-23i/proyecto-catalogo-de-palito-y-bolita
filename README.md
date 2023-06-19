Reporte -Trabajo Final-

-Nombre:-Pimentel Cruz Abdiel Yared 
        -Rodríguez Muñoz Erik
      
-Matricula: -2223068588
            -2223068499
            
-Objetivo- 
El proyecto consiste en estructurar un código en python el cual sea capaz de cumplir con lo siguiente, el código debe  ser capaz de crear un catálogo ya sea importado o agregado por el usuario el cual categorice el título seleccionado, es decir que sea película, serie, documental, entre otros. Además de mostrar cierta información como el costo de venta, renta, temporadas, director, actor, entre otros dependiendo del título seleccionado. El código debe cumplir con funciones como agregar títulos, eliminar títulos, buscar títulos, y por supuesto guardar los títulos ingresados. 

-Diagrama de estructura-

------------------------------ 
{         Archivo            } <--------------------------------------------------------------------
{----------------------------}                                                                      |
{                            }                                                                      |
{ Guardar el catálogo creado } <--------------------------                                          |
{ en un archivo txt.         }                            |                                         |
{----------------------------}                            |                                         |
              |                                           |                                         |
              |                                           |                                         |
-----------------------------               ----------------------------               ----------------------------
{         Catálogo           }              {         Agregar          }               {        Eliminar          }
{----------------------------}              {------------------------- }               {--------------------------}
{                            }              { Agregar diferentes       }               { Elimina un título        }
{ Guardar y categorizar la   }  ----------> { títulos dentro del       } ------------> { seleccionado del         }
{ informacion del catálogo.  }              { catálogo.                }               { catálogo.                }
{----------------------------}              {--------------------------}               {--------------------------}
              |                 \
              |                   \ 
              |                     \
-----------------------------         \     ----------------------------               ----------------------------
{         Búsqueda           }         ---> {         Main             }               {        Mostrar           }
{----------------------------}              {------------------------- }               {--------------------------}
{                            }              { Script principal el cuál }               {                          }
{ Busca un título dentro del }  ----------> { funciona gracias a todos } ------------> { Muestra los menús y los  }
{ catálogo.                  }              { los demás scripts.       }               { catálogos disponibles.   }
{----------------------------}              {--------------------------}               {--------------------------}
 
 
 
 El diagrama anterior muestra de forma sencilla y efectiva los diferentes scripts que corresponden al código realizado, cada script se encarga de realizar una función diferente y simplificar la dificultad del código. Al ver el diagrama, podemos ver de forma rápida las diferentes funciones que podrá realizar y el cómo es que decidimos separarlas para implementarlo.
 
 -Uso de módulos y programa principal-

Dentro de nuestro código, decidimos dividir las tareas que debería realizar el código para poder dar una estructura más limpia y sencilla. A continuación explicaremos las diferentes funciones de los scripts 

Agregar: Este script se encarga de agregar los títulos, el director, el año, las temporadas. Y además agregarlos a la categoría que corresponda. 
Archivo: Este script es más sencillo ya que se encarga de guardar los elementos que agregues al catálogo, y crear un archivo que los contenga para luego poder importarlos al programa. 
Eliminación: Este script se encargará de eliminar un título seleccionado junto con su información correspondiente. 
Catálogo: Este script es uno de los principales ya que se encarga de guardar la información de los títulos y ordenarla. 
Búsqueda: Este script más sencillo, tiene la función de buscar dentro del catálogo un título de acuerdo a el título seleccionado de dicho catálogo. 
Main: Este es el script principal del programa ya que es el que llevará el menú principal desde donde podrás realizar las demás funciones dentro del programa. 
Mostrar: Mostrar es el script que llevará a cabo la función de mostrar el catálogo y menús dependiendo de la categoría que el usuario deseé ver o revisar.

El programa principal es el que tiene el nombre de “main” ya que se encarga de mostrar el menú principal, importar los demás script y dependiendo de lo que quiera el usuario, ejecutará los demás scripts.

-Comentarios del diseño y de la implementación-

El programa cuenta con un diseño Top Down, y con una estructura de control selectiva.
 Decidimos hacer uso del Top Down ya que queríamos realizar un código sencillo de leer y fácil de revisar en caso de tener algún error, de esta forma también podemos editar la estructura  y modificar las funciones que debe realizar por separado y que sea más fácil volver a ejecutarlo, como ya sabemos el diseño Top Down consiste en dividir el programa principal en programas más sencillos de realizar y ejecutar. La estructura de control selectiva se encargaría de poder crear las categorías del catálogo y además poder acceder a todas las diferentes funciones de nuestro programa.  Es por ello que optamos por utilizar este diseño, ya que con ello conseguimos dividir el programa como queríamos desde el principio.

El cómo lo implementamos fue más sencillo, ya que teniendo en cuenta que nuestro programa debe realizar diferentes tareas, decidimos dividirlo de acuerdo a las tareas que debe realizar. Primero separamos las funciones necesarias, es decir que si debíamos agregar o eliminar un producto del catálogo entonces creamos un script para eliminar y uno para agregar, pero claro no todas las características están por separado, tambien algunas las mantuvimos dentro de un script para poder llevar a cabo una revisión más efectiva, es decir que no optamos por dividir las categorías del catálogo por ejemplo, si no que en un mismo script se encuentra todo el catálogo pero en diferentes categorías,para ello fue que utilizamos el uso de estructura de control selectiva con ello lo que logramos es que las funciones que se deben realizar, están por separado, pero los scripts principales que se encargan de mostrar los catálogos están en un mismo script y así poder modificar con mayor eficiencia.
Implementado de esta forma conseguimos hacer modificaciones mínimas gracias a tener todo ordenado y separado, logramos incluso modificar las funciones sin tener que tocar los scripts de menú o de catálogo.





