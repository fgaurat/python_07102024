class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        if longueur<=0:
            raise Exception('longueur <=0')
        self.__longueur = longueur

    def set_largeur(self,largeur):
        if largeur<=0:
            raise Exception('longueur <=0')
        self.__largeur = largeur
    
    def get_surface(self):
        return self.__largeur*self.__longueur
    
    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self,o):
        assert isinstance(o,Rectangle)
        # if not isinstance(o,Rectangle):
        #     raise TypeError("not a Rectangle")
        return self.__longueur == o.__longueur and self.__largeur == o.__largeur
    
    longueur = property(get_longueur,set_longueur,doc="Longueur property")
    largeur = property(get_largeur,set_largeur,doc="Largeur property")