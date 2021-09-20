import os
from unittest import main
from flask import Flask, jsonify, request
from math import sqrt
import unittest
from abc import ABCMeta, abstractmethod

class Calculadora (object):

    def calculadora(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else: 
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica (object):

    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()      
        elif (operador == 'multiplicacao'):
             return Multiplicacao()

class Operacao(metaclass=ABCMeta):

    @abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao): 
      def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado
    
class Divisao(Operacao): 
      def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Multiplicacao(Operacao): 
      def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado  


class Testes(unittest.TestCase):
    def test_somar(self):
        calculador = Calculadora()
        result = calculador.calculadora(2,3, 'soma')
        self.assertEqual(result, 5) 

    def test_subtracao(self):
        calculador = Calculadora()
        result = calculador.calculadora(2,3, 'subtracao')
        self.assertEqual(result, -1)     

    def test_divisao(self):
        calculador = Calculadora()
        result = calculador.calculadora(2,4, 'divisao')
        self.assertEqual(result, 0.5)
        
    def test_multiplicacao(self):
        calculador = Calculadora()
        result = calculador.calculadora(2,3, 'multiplicacao')
        self.assertEqual(result, 6)        

ObjetoCalculadora = Calculadora()
print(ObjetoCalculadora.calculadora(10,20,'soma'))

if __name__ == '__main__':
    main()
