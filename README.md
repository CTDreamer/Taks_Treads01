# Taks_Treads01 🚀

Descripción
Este es una tarea para el curso de Programación Paralela 🧑‍💻, donde implementamos un algoritmo para encontrar números primos de forma secuencial y paralela. La idea es aprovechar múltiples hilos de ejecución (usando Python), para acelerar el proceso de búsqueda de números primos en un rango grande de números (hasta N).

El código compara el rendimiento de las dos estrategias: secuencial y paralela, mostrando los tiempos de ejecución de cada enfoque. Si tienes dudas sobre paralelismo o hilos, ¡este proyecto es un excelente punto de partida!

Tecnologías Usadas 🔧
Python 3.x: El lenguaje principal utilizado para el desarrollo del código.

Bibliotecas de Python:

math: Para realizar cálculos matemáticos, como calcular la raíz cuadrada, lo que optimiza la búsqueda de números primos.

concurrent.futures: Usado para crear y manejar hilos de manera sencilla, lo que permite paralelizar la búsqueda de primos.

time: Para medir el tiempo de ejecución y hacer comparaciones entre la ejecución secuencial y la paralela.

Objetivo 🎯
El objetivo de este proyecto es demostrar cómo podemos mejorar el rendimiento de algoritmos, como la búsqueda de números primos, mediante paralelismo. Al dividir el trabajo entre múltiples hilos, se reduce el tiempo de ejecución, lo que se nota especialmente cuando el rango de números es grande.

Resumen del Código 💻
Este proyecto tiene dos enfoques para encontrar números primos:

Enfoque Secuencial:

Recorre cada número en el rango de 2 a N.

Verifica si cada número es primo utilizando la función es_primo.

Enfoque Paralelo:

Divide el rango de 0 a N en bloques.

Asigna cada bloque a un hilo de ejecución (usando ThreadPoolExecutor).

Cada hilo busca los primos en su respectivo bloque, y al final se combinan los resultados.

¿Cómo funciona el código?
Verificación de Primos:

La función es_primo se encarga de verificar si un número es primo.

Se usa la técnica de verificar hasta la raíz cuadrada del número, lo que hace la verificación mucho más rápida.

Búsqueda Secuencial:

Usamos un simple bucle for para recorrer los números del rango.

Si el número es primo, lo agregamos a la lista de primos.

Búsqueda Paralela:

El rango de números se divide en bloques, y cada bloque es procesado por un hilo.

Usamos ThreadPoolExecutor para manejar la creación y ejecución de los hilos de manera eficiente.

Los resultados de todos los hilos se combinan al final.

Comparación de Tiempos:

El código mide el tiempo que tarda en hacer la búsqueda de primos, tanto secuencial como paralelamente, para que puedas ver la diferencia en rendimiento.

Autor 📚
Cristhian Anthony Torres Tineo
Código de alumno: 22200050
Profesor: Jorge Luis Chávez Soto
Curso: Programación Paralela

Cómo ejecutar el proyecto 🏃‍♂️
Asegúrate de tener Python 3.x instalado en tu máquina.

Clona el repositorio o descarga los archivos.

Navega a la carpeta del proyecto en tu terminal.

Ejecuta el código con:

bash
Copiar
python3 nombre_del_archivo.py
Si todo está bien, verás los números primos encontrados, junto con los tiempos de ejecución secuenciales y paralelos.
