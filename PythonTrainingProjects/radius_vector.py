import math


class RadiusVector:
    def __init__(self, *args):
        self.__grade = 0
        self.__coords = ()
        if len(args) == 1 and type(args[0]) is int:
            self.__grade = args[0]
            self.__coords = tuple([0 for i in range(0, args[0])])
        else:
            res = []
            for c in args:
                res.append(c)
            self.__grade = len(res)
            self.__coords = tuple(res)
    

    def set_coords(self, *coords):
        res = []
        c_len = 0
        for c in coords:
            c_len += 1
        for i in range(0, self.__grade):
            if i < c_len:
                res.append(coords[i])
            else:
                res.append(self.__coords[i])
            i += 1

        self.__coords = tuple(res)
    

    def get_coords(self):
        return (c for c in self.__coords)
    

    def __len__(self):
        return self.__grade
    
    
    def __abs__(self):
        res = 0
        for coord in self.get_coords():
            res += coord*coord
        return math.sqrt(res)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
print(a, b, c)
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
a, b, c = vector3D.get_coords()
print(a, b, c)
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
a, b, c = vector3D.get_coords()
print(a, b, c)
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)

print(res_len, ' ', res_abs)