# **Python**

Carpeta destinada a contener documentación y ejercicios en Python

# **¿Qué es Python?**

Lenguaje interpretado, a diferencia de un ensamblador que son 
lenguajes de bajo nivel que se basan en la mnemotecnia para programar 
directamente en microprocesadores, y de un compilador que tiene varias 
capaz de validación y generan binarios para cada plataforma. Los 
lenguajes interpretados son traducidos a lenguaje de maquina en tiempo 
de ejecución. Esto los hace mas lento pero mas versátiles para ser 
ejecutados en cualquier máquina.

## Características

Multi-paradigma, soporta los siguientes paradigmas  

- POO
- Imperativa
- Funcional

Sin embargo, puede adoptar mas usando librerías u addons.

Identado, es decir que en vez de usar ; para separar sus instrucciones 
este usa tabulaciones.

# **¿Cómo usarlo?**

En este caso no instalaremos python directamente sino que usaremos un contenedor de librerías de python, dentro del cual estará instalado una version especifica de este. Así, tendremos ordenado y limpio nuestro entorno de trabajo, separándole de los demás. 

## **Conda**

Conda es un administrador de entornos virtuales para python.
En este, se administran las librerías que se usaran.
A modo de ejercicio solo se establecerá un entorno virtual que contendrá todas las librerías que los ejercicios usen.

Comandos comunes en Conda:

 - Crear un entorno virtual  
`conda create -n nombre_del_entorno`
 - Crear un entorno virtual desde un archivo.  
`conda create -n nombre_del_entorno --file nombre_del_archivo.extensión`
 - Activar un entorno       
`conda activate nombre_del entorno`
 - Agregar un channel       
`conda config --add channel canal_a_agregar`
 - Mostrar los canales  
`conda config --show channels`
 - Instalar una librería  
`conda install nombre_del_paquete`
 - Desinstalar una librería  
`conda uninstall nombre_del_paquete`
 - Listar las librerías del entorno  
`conda list`

## **Entorno**

El entorno para este ejercicio se llamara practica

Para activarlo se debe ejecutar el comando 
`conda activate practica`
o créalo usando
`conda create -n practica`  
o  
`conda create -n practica --file requeriments.txt.`










