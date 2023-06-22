Reporte -Trabajo Final-

-Nombre:-Pimentel Cruz Abdiel Yared 
        -Rodríguez Muñoz Erik
      
-Matricula: -2223068588
            -2223068499

-Profesor: Abel García Nájera
            
El proyecto consiste en estructurar un código en phyton el cuál sea capaz de cumplir con lo siguiente, el código debe ser capaz de 
crear un catálogo ya sea importado o agregado por el usuario, el cuál categorice los títulos seleccionados, dependienso de si es 
película, serie, documental o evento en vivo. Además de que tambíen debe mostrar información de cada título como:
costo de venta, costo de renta, director, año, temporadas, actor principal, fecha, entre otros. El código debe cumplir con funciones 
como agregar títulos, eliminar títulos, buscar títulos y tambien crear, guardar e importar los catálogos creados.

-Diagrama de Estructura-  
 
 
 El diagrama anterior muestra 
 
 -Uso de módulos y programa principal-

Dentro de nuestro código, decidimos dividir las tareas que debería realizar el código para poder dar una estructura más limpia y sencilla. A continuación explicaremos las diferentes funciones que realiza nuestro programa. 

Agregar: Esta se encarga de agregar los títulos, el director, el año, las temporadas. Y además agregarlos a la categoría que corresponda. 
Archivo: Esta es más sencilla ya que se encarga de guardar los elementos que agregues al catálogo, y crear un archivo que los contenga para luego poder importarlos al programa. 
Eliminación: Esta se encargará de eliminar un título seleccionado junto con su información correspondiente. 
Búsqueda: Esta es más sencilla, tiene la función de buscar dentro del catálogo un título de acuerdo a el título seleccionado de dicho catálogo. 
Main: Este es el script principal del programa ya que es el que importara los scripts creados desde donde podrás realizar todas las demás funciones dentro del programa. 

En el programa ya corregido y simplificado, utilizamos unicamente 4 scripts que son aquellos que contienen las funciones descritas anteriormente.

A continuacion explicaremos los scripts:
"Main"
El script principal es el que tiene el nombre de “main” ya que se encarga de importar todos los demas scripts y dependiendo de lo que el usuario requiera, ejecutará los demás scripts.
"main" cuenta con el menú principal del programa, su funcionamiento es facil, el usuario selecciona la opcion que desea ejecutar, y el script "main" manda la informacion a otro modulo, en donde se realizará la siguiente acción. 
"Catálogo"
Dentro de este script, podemos notar que hay más líneas de código, esto debido a que para poder simplificar mas nuestro programa, decidimos estructurar de la siguente forma el script:
Dentro de este podras encontrar las funciones de "catálogo_principal" el cual se encarga de, principalmente acomodar y mostrar el catálogo con sus productos, dentro de este script se organizan todas las categorias adecuadas dependiendo de el tipo de producto, ademas de que tambien cuenta con la funcion definida para poder implementar nuevos productos al catálogo. El script se encarga de crear listas categorizadas para poder guardar la informacion completa de todos los productos que contiene y agregar aun mas productos. 
"Buscar y Eliminar" 
El script aqui, es mucho mas sencillo ya que se encargará de realizar 2 tareas unicamente, la primer tarea es poder buscar dentro de las listas algun producto mediante una palabra clave, y la segunda tarea, que es la de eliminar se encarga de seleccionar un producto en especifico y eliminarlo de las listas del catálogo.
"Archivo"
Por último, el script "archivo" tambíen realiza 2 tareas, las cuales son escenciales para el programa, las cuales consisten en tomar la información de un catálogo que pueda crear un usuario y guardarla en un archivo.txt, por supuesto asi como tiene la tarea de crear catálogos, tambíen cuenta con la funcion de poder importar un archivo en formato .txt y además implementar esa informacion dentro del catálogo. 
Estos son los módulos que componen nuestro programa. 

-Comentarios del diseño y de la implementación-

El programa cuenta con un diseño Top Down, y con una estructura de control selectiva.
Decidimos hacer uso del Top Down de fórma que queríamos realizar un código sencillo de leer y fácil de revisar en caso de tener algún error, de esta forma también podemos editar la estructura  y modificar las funciones que debe realizar por separado y que sea más fácil volver a ejecutarlo, como ya sabemos el diseño Top Down consiste en dividir el programa principal en programas más sencillos de realizar y ejecutar. La estructura de control selectiva se encargaría de poder navegar dentro del catálogo y además poder acceder a todas las diferentes funciones de nuestro programa.  Es por ello que optamos por utilizar este diseño, ya que con ello conseguimos dividir el programa como queríamos desde el principio.

Para poder implementar correctamente cada módulo, debemos definir las funciones que realizarán las acciones necesarias, pero claro antes de ello debemos entender que, nuestro código funciona gracias a la implementación de if y else para poder elegir entre diferentes opciones dentro de los menús del catálogo, de esta forma es fácil manipular y navegar por el menú ya que cada acción se encuentra concatenada a una función previamente definida o también a otro menú, dependiendo de lo que el usuario solicite. 

En pocas palabras, la forma de navegar dentro de nuestro programa es gracias a la estructura de control selectiva y la fórma de ejecutar acciones es gracias a la definición previa de funciones. 

Para poder implementarlo de una mejor manera que la anterior, decidimos reducir los módulos que contenia el programa, asi podriamos tener menos modulos. La implementación consiste en crear dentro de un script una o varias funciones que realicen una tarea en específico, los scripts funcionan gracias a un script principal el cual tiene la funcion de concatenar todos los demas y asi mandar informacion de un script a otro y regresarla con la función ya efectuada. Definimos una funcion para cada tarea a realizar, y por lo tanto para cada instruccion que se le de al programa, este ejecutara la funcion adecuada. 





