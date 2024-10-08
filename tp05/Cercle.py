from ICalcGeo import ICalcGeo
import math

class Cercle(ICalcGeo):
    
    def __init__(self,rayon=1):
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon
    
    @rayon.setter
    def rayon(self,rayon):
        if rayon<=0:
            raise Exception('rayon <=0')
        self.__rayon = rayon
    
    # @property
    def surface(self):
        return math.pi*self.__rayon**2