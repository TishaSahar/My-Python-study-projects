import math

class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img


    @property
    def real(self):
        return self.__real
    
    @real.setter
    def real(self, value):
        if type(value) in (int, float):
            self.__real = value
        else:
            raise ValueError('Неверный тип данных')
    
    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self.__img = value
        else:
            raise('Неверный тип данных')


def abs(cm):
    r  = cm.real
    i = cm.img
    return math.sqrt(r*r + i*i)


def main():
    cmp = Complex(7, 8)
    cmp.real = 3
    cmp.img = 4
    c_abs = abs(cmp)


if __name__ == '__main__':
    main()