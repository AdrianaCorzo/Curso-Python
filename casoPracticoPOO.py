import random

class Matriz():
    #Constructor
    def __init__(self,n_t_matriz):
        self.n_t_matriz = n_t_matriz
        self.matriz = self.crear_matriz()

    #Métodos
    """ 
    1.Crea la Matriz cuadrada de tamaño igual al Args: n_t_matriz 
    y la llena con números aleatorios del 0 al 9
    """
    def crear_matriz(self):
        matriz = []
        for _ in range(self.n_t_matriz):
            fila = []
            for _ in range(self.n_t_matriz):
                #Añadimos números aleatorios para llenar la fila
                fila.append(random.randint(0, 9))
            matriz.append(fila)
        return matriz

    #2.Imprime una Matriz  
    def imprimir_matriz(self):
        print("Matriz Generada")
        for fila in self.matriz:
            print(fila)

    #3.Suma e imprime el total de las filas y las columnas
    def suma_columnas_filas(self):
        suma_filas = [sum(fila) for fila in self.matriz]
        suma_columnas = [sum(columna) for columna in zip(*self.matriz)]
        return suma_filas,suma_columnas

"""
Función para pedir el número del tamaño de la matriz y válida que sea un entero mayor o igual a 0
Manejo de la excepción cuando se ingresa un valor no númerico para crear la matriz
"""
def pedir_numero():
    while True:
        try:
            n_t_matriz = int(input("\nIngrese el tamaño de la matriz (0 para salir): "))
            if n_t_matriz >= 0:
                return n_t_matriz
            else:
                print('\nError: Debe ingresar un número entero positivo o 0 para salir de la aplicación.')
        except ValueError:
            print('\nError: Debe ingresar un número entero positivo o 0 para salir de la aplicación.')

"""
Bloque principal: se crea un bucle para que el programa se ejecute hasta que el usuario ingrese 0
para Salir y terminar la aplicación
"""

if __name__ == '__main__':
    continuar = True
    while continuar:
        n_t_matriz = pedir_numero()
        if n_t_matriz == 0:
            print('Salir de la aplicación')
            continuar = False
        else:
            matriz_generada = Matriz(n_t_matriz)
            matriz_generada.imprimir_matriz()
            suma_fila, suma_col = matriz_generada.suma_columnas_filas()
            print(f'\nTotal Filas: {suma_fila} \nTotal Columnas: {suma_col}')