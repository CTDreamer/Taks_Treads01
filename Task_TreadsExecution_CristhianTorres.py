import math
import concurrent.futures
import time

# Función para verificar si un número es primo
# Esta función revisa si un número es primo al verificar si es divisible
# por algún número entre 2 y su raíz cuadrada. Esto es más eficiente
# que verificar hasta el número mismo.
def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# Función secuencial para buscar primos en un rango
# Aquí recorremos cada número del rango dado, verificamos si es primo
# usando la función `es_primo` y agregamos los primos encontrados a una lista.
def buscar_primos_secuencial(rango):
    primos = []
    for num in rango:
        if es_primo(num):
            primos.append(num)
    return primos

# Función para buscar primos en un rango de manera paralela
# Esta función divide el rango de 0 a N en bloques y asigna cada bloque
# a un hilo de ejecución. Cada hilo busca primos dentro de su bloque de números.
# Después, los resultados de todos los hilos se combinan en una sola lista.
def buscar_primos_paralelo(N, num_hilos=4):
    bloque_size = N // num_hilos  # Calculamos el tamaño de cada bloque
    bloques = [(i * bloque_size, (i + 1) * bloque_size) for i in range(num_hilos)]  # Creamos los bloques
    bloques[-1] = (bloques[-1][0], N + 1)  # Aseguramos que el último bloque cubra hasta N

    # Usamos ThreadPoolExecutor para crear un grupo de hilos
    # Cada hilo trabaja con un bloque de números
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_hilos) as executor:
        # Asignamos a cada hilo una parte del rango para buscar primos
        futures = [executor.submit(buscar_primos_secuencial, range(bloque[0], bloque[1])) for bloque in bloques]
        
        primos = []  # Lista donde vamos a acumular los primos encontrados por todos los hilos
        for future in concurrent.futures.as_completed(futures):  # Esperamos a que todos los hilos terminen
            primos.extend(future.result())  # Agregamos los resultados de cada hilo

    return primos  # Retornamos todos los primos encontrados

# Función para comparar los tiempos de ejecución secuenciales y paralelos
# Compara el tiempo de ejecución de la búsqueda secuencial (un solo hilo)
# y la búsqueda paralela (multiples hilos), imprimiendo los tiempos y los resultados.
def comparar_tiempos(N, num_hilos=4):
    start_time = time.time()  # Iniciamos el cronómetro para la ejecución secuencial
    primos_secuenciales = buscar_primos_secuencial(range(2, N + 1))  # Realizamos la búsqueda secuencial
    secuencial_time = time.time() - start_time  # Calculamos el tiempo que tomó la búsqueda secuencial

    start_time = time.time()  # Iniciamos el cronómetro para la ejecución paralela
    primos_paralelos = buscar_primos_paralelo(N, num_hilos)  # Realizamos la búsqueda paralela
    paralelo_time = time.time() - start_time  # Calculamos el tiempo que tomó la búsqueda paralela

    # Imprimimos los resultados y tiempos
    print(f"Primos encontrados: {primos_secuenciales}")
    print(f"\nTiempo de ejecución secuencial: {secuencial_time:.6f} segundos")
    print(f"Tiempo de ejecución paralelo: {paralelo_time:.6f} segundos")

# Bloque principal
# Aquí se define el valor de N (el rango hasta el que buscaremos primos) y el número de hilos que usaremos.
# Después, llamamos a la función que compara los tiempos y hace todo el trabajo.
if __name__ == "__main__":
    N = 1000000  # El rango hasta el cual buscaremos primos
    num_hilos = 16  # Número de hilos para la paralelización
    comparar_tiempos(N, num_hilos)  # Llamamos a la función para comparar tiempos
