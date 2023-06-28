from functools import partial

class Imaginario:
    __real=0
    __imaginario=0
    def __init__(self, real, imaginario):
        self.__real = real
        self.__imaginario = imaginario

    def __add__(self, otro):
        real = self.__real + otro.real
        imaginario = self.__imaginario + otro.imaginario
        return Imaginario(real, imaginario)

    def __sub__(self, otro):
        real = self.__real - otro.real
        imaginario = self.__imaginario - otro.imaginario
        return Imaginario(real, imaginario)

    def __mul__(self, otro):
        real = self.__real * otro.real - self.__imaginario * otro.imaginario
        imaginario = self.__real * otro.imaginario + self.__imaginario * otro.real
        return Imaginario(real, imaginario)

    def __truediv__(self, otro):
        denominador = otro.real ** 2 + otro.imaginario ** 2
        real = (self.__real * otro.real + self.__imaginario * otro.imaginario) / denominador
        imaginario = (self.__imaginario * otro.real - self.__real * otro.imaginario) / denominador
        return Imaginario(real, imaginario)
        