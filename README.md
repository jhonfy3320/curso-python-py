# curso-python-py
# estamos creando un  proyecto para este curso de entornos virtuales 

# game piedra papel tijera 

para correr el juego debes seguir las siguientes instrucciones en la terminal 

```sh
cd game
python3 main.py
```

# descripción 
README.md es un archivo de texto que se encuentra en la raíz de muchos repositorios de software en GitHub. El archivo README se utiliza para proporcionar información general sobre el proyecto y orientar a otros desarrolladores o usuarios sobre cómo utilizar y contribuir al proyecto.

Un archivo README suele contener información como:

Descripción del proyecto: un resumen de lo que hace el proyecto y para qué se utiliza.
Requisitos: una lista de dependencias y requisitos del sistema necesarios para ejecutar el proyecto.
Instalación: instrucciones para instalar y configurar el proyecto en una máquina local.
Uso: instrucciones para ejecutar el proyecto y utilizar sus funcionalidades.
Contribución: instrucciones para aquellos interesados en contribuir al proyecto, como guías de estilo y procesos de revisión.
Licencia: información sobre la licencia bajo la cual se distribuye el proyecto.
El archivo README se escribe en formato de marcado de texto (Markdown), lo que permite utilizar formateo y enlaces para mejorar la legibilidad del texto. Es común que el archivo README se muestre automáticamente en la página principal del repositorio en GitHub para facilitar el acceso a esta información.
 

# entornos virtuales con python 

Creando ambientes virtuales con python

Abre una terminal o una ventana del símbolo del sistema.

Navega hasta el directorio donde quieres crear el ambiente virtual. Por ejemplo, puedes usar el comando cd para cambiar de directorio.

Escribe el siguiente comando y presiona Enter:

{python3 -m venv nombre_del_ambiente}

Reemplaza nombre_del_ambiente con el nombre que quieres dar al ambiente virtual. Este comando creará un directorio con el nombre especificado que contendrá una instalación de Python y los archivos necesarios para el ambiente virtual.

Para activar el ambiente virtual, ejecuta el archivo activate que se encuentra en el directorio bin del ambiente virtual. En Windows, puedes hacerlo de la siguiente manera:

{nombre_del_ambiente\Scripts\activate.bat}

En Linux o macOS, puedes hacerlo de la siguiente manera:

{source nombre_del_ambiente/bin/activate}

Una vez que hayas activado el ambiente virtual, todas las operaciones de Python que realices estarán aisladas en ese ambiente y no afectarán al resto de tu sistema. Para desactivar el ambiente virtual, simplemente escribe el comando deactivate y presiona Enter.

__Si quieres instalar paquetes adicionales en el ambiente virtual, puedes usar el comando pip install como de costumbre. Por ejemplo, para instalar el paquete numpy, escribe pip install numpy y presiona Enter.
__

# comandos para crear entornos virtuales con python 
Hola Chicos! 😄
Verificar donde esta python y pip

which python3

which pip3

Si estas en linus o wsl debes instalar

sudo apt install -y python3-venv
Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

python3 -m venv env
Activar el ambiente

source env/bin/activate
Salir del ambiente virtual

deactivate
Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo

pip3 install matplotlib==3.5.0
Verificar las instalaciones

pip3 freeze