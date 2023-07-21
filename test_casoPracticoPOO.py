import unittest
from unittest.mock import patch
from casoPracticoPOO import Matriz

class TestMatriz(unittest.TestCase):

    def setUp(self):
        #Se crea una instancia de la clase Matriz con tamaño = 3
        self.matriz_prueba = Matriz(3)

    def test_crear_matriz(self):
        #Verificamos que la Matriz creada tenga el tamaño correcto 3x3
        self.assertEqual(len(self.matriz_prueba.matriz), 3)
        for fila in self.matriz_prueba.matriz:
            self.assertEqual(len(fila), 3)

    def test_suma_columnas_filas(self):
        #Verificamos que la función suma_columnas_filas se ejecute correctamente
        
        #Se crea una matriz 3x3
        matriz_esperada =[[8,0,8],[0,1,7],[6,9,3]]
        # se calcula la suma de filas y columnas para compararla con los resultados de la función
        s_fila_esperada = [16,8,18]
        s_col_esperada = [14,10,18]

        #Establecemos la matriz esperada en la instancia de la clase Matriz
        self.matriz_prueba.matriz = matriz_esperada

        #LLamamos al método y comparamos los resultados con los esperados
        suma_filas, suma_columnas = self.matriz_prueba.suma_columnas_filas()
        
        self.assertEqual(suma_filas, s_fila_esperada)
        self.assertEqual(suma_columnas, s_col_esperada)
        

    

if __name__ == '__main__':
    unittest.main()

