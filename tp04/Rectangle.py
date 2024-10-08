class Rectangle:
    __slots__ = ('__longueur','__largeur')
    __cpt = 0 
    def __init__(self,longueur=1,largeur=1):
        self.__longueur=longueur
        self.__largeur=largeur
        Rectangle.__cpt+=1
    
    def __del__(self):
        print("def __del__(self)")
        Rectangle.__cpt-=1
    
    @classmethod
    def buildFromStr(cls,value):
        values = [int(i) for i in value.split(',')]
        # r = cls(values[0],values[1])
        r = cls(*values)
        return r
    
    @staticmethod
    def get_cpt():
        return Rectangle.__cpt

    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,longueur):
        if longueur<=0:
            raise Exception('longueur <=0')
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        if largeur<=0:
            raise Exception('longueur <=0')
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__largeur*self.__longueur
    
    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self,o):
        assert isinstance(o,Rectangle)
        # if not isinstance(o,Rectangle):
        #     raise TypeError("not a Rectangle")
        return self.__longueur == o.__longueur and self.__largeur == o.__largeur
    