## ToDo List

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)![Static Badge](https://img.shields.io/badge/Date_Release-Junio-orange)![Static Badge](https://img.shields.io/badge/ToDo_List-%20V1.0.0-blue)

## Índice

*[Título e imagen de portada](#Título-e-imagen-de-portada)

*[Insignias](#insignias)

*[Índice]()

*[Descripción del proyecto](#descripción-del-proyecto)

*[Estado del proyecto](#estado-del-proyecto)

*[Características de la aplicación y demostración](#características-de-la-aplicación-y-demostración)

*[Acceso al proyecto](#acceso-al-proyecto)

*[Tecnologías utilizadas](https://github.com/DamianRojas79/ToDo-List/edit/main/README.md#tecnolog%C3%ADas-utilizadas-heavy_check_mark)  

*[Personas desarrolladores del proyecto](#personas-desarrolladoras-del-proyecto)

*[Licencia](licencia-)

*[Conclusión](#conclusión)

  
## Descripción del Proyecto

Todolist es una aplicación que permite llevar un registro de tus tareas y tener una vista general de tus responsabilidades. <br><br>

 
![image alt](https://github.com/DamianRojas79/ToDo-List/blob/main/images-git/Imagen%20pegada.png)

  
  

## Estado del Proyecto

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)


  

## Características de la aplicación y demostración

  

:hammer: **Funcionalidades del proyecto**

- `Funcionalidad 1`: **Registrarse** <br>

La aplicación permite "Registrarse" en la pantalla de inicio. Para crear un nuevo usuario solo se ingresa el nombre de usuario y la contraseña. <br><br>

  

![image alt](https://github.com/DamianRojas79/ToDo-List/blob/main/images-git/registrarse.png)

  

- `Funcionalidad 2`: **Iniciar sesión** <br>

Si ya tienes un usuario registrado puedes "iniciar sesión" desde la pantalla de inicio.

  

![image alt](https://github.com/DamianRojas79/ToDo-List/blob/main/images-git/inciar_sesion.png)

  
  

- `Funcionalidad 3`: **Visualizar tareas**<br>

Una vez registrado en la pantalla principal se pueden ver las tareas que tiene registradas el usuario. Allí también se puede de modificar, editar y crear una nueva tarea.

  

![image alt](https://github.com/DamianRojas79/ToDo-List/blob/main/images-git/lista_tareas.png)

  

- `Funcionalidad 4`: **Ingresar nueva tarea** <br>

Para ingresar una nueva tarea se debe seleccionar la opción "Nuevo" en la pantalla principal. Los datos que se solicitan para una nueva tarea son el "Título" y "Descripción" de la nueva tarea.

  
  

![image alt](https://github.com/DamianRojas79/ToDo-List/blob/main/images-git/nueva_tarea.png)

  

- `Funcionalidad 5`: **Editar tarea** <br>´

Se puede editar una tarea ya registrada ya sea su título o descripción ingresando a la opción "Editar" desde la pantalla principal.


  
![image alt](https://github.com/DamianRojas79/ToDo-List/blob/main/images-git/editar_tarea.png)

  

- `Funcionalidad 6`: **Eliminar Tarea** <br>

Se puede eliminar una tarea desde la pantalla principal con el boton "Eliminar".

  
  

- `Funcionalidad 7`: **Cambiar de estado una tarea** <br>

Las tareas pueden cambiar su estado desde la pantalla de "Editar", allí se puede pasar a un estado completado selecionando el check "Completado".<br>

Las tareas por defecto quedan con un estado inicial "incompleto" cuando son ingresadas.
<br><br>
  
  

## Acceso al Proyecto

  

Para descargar y ejecutar el proyecto se debe realizar los siguientes pasos:

  

:file_folder: **Acceso al proyecto**

- **Abrir terminal**<br>

Primero se debe abrir una terminal para ejecutar los comandos necesarios para descargar y ejecutar el proyecto.

  

- **Crear directorio para el proyecto**<br>

Ejecutar:<br>

<i>mkdir proyecto-todolist</i>

  

- **Clonar repositorio**<br>

Para clonar el repositorio primero situarse en el directorio creado:<br>

Ejecutar:<br>

<i>cd proyecto-todolist </i><br>

Luego allí clonar el repositorio:<br>

Ejecutar:<br>

<i>git clone git@github.com:DamianRojas79/ToDo-List.git </i>

  

:hammer_and_wrench: **Abre y ejecuta el programa**

- **Instalar python y modulo venv para crear entornos virtuales**<br>

Para instalar Pyhton

Ejecutar:

<i>sudo apt install python3</i> <br>

  

Para instalar venv

Ejecutar:

<i>sudo apt install -y python3-venv</i><br>

  
  
  

- **Crear entorno virtual para el proyecto**<br>

Se crea un entorno virtual para tener allí todos los paquetes necesarios para el proyecto.<br>

Para ello primero se debe entrar al directorio clonado.<br>

Ejecutar:

<i>cd ToDo-List </i>

  

Luego se crea el entorno virtual:

Ejecutar:

<i>python -m venv env-todo</i>

  

- **Activar entorno virtual**

Ejecutar:

<i>source env-todo/bin/activate</i>

  

- **Instalar las dependencias para el proyecto**<br>

Se instalan las as dependencias necesarias que se encuentra dentro del archivo requirements.txt.<br>

Ejecutar:<br>

<i>pip install -r requirements.txt</i>

  

- **Ejecutar el programa**

Ejecutar:

<i>Python3 run.py</i>

  

- **Abrir aplicación en el navegador**<br>

En el navegador que desee ingresar la siguiente URL para abrir la aplicación:<br>

http://localhost:5000/

  

## Tecnologías Utilizadas :heavy_check_mark:

- **HTML**<br>

- **Boostrap**<br>

- **Flask**<br>

- **Blueprint**<br>

- **Jinja**<br>

- **Flask-SQLAlchemy**<br>

- **Sqlite**<br>

  

## Personas Desarrolladoras del Proyecto

[<img src="https://avatars.githubusercontent.com/u/135189204?s=400&u=932907d7db09c6472e34c43c6b5ed27be7342bf4&v=4" width=115><br><sub> Damian Rojas </sub>](https://github.com/DamianRojas79)

## Licencia 📄
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

  
Este proyecto cuenta con licencia conforme a los términos de la licencia MIT.  
  
## Conclusión
**Todo List** es un desarrollo de media complejidad que además de la funcionalidad en si que esta ofrece permite mostrar la utilización de las diferentes tecnologías que en ella se encuentran. En esta primera etapa se cumplió con las necesidades básicas del proyecto para dar una primera versión de la misma. 

