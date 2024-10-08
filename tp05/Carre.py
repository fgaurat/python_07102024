from Rectangle import Rectangle
class Carre(Rectangle):
    
    def __init__(self,cote=1):
        super().__init__(cote,cote)
        self.__cote = cote
        
    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self,cote):
        if cote<=0:
            raise Exception('cote <=0')
        self.__cote = cote
        self.longueur = cote
        self.largeur = cote