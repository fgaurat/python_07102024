from Carre import Carre
from Cercle import Cercle
def main():
    c = Carre(5)
    print(c.surface )
    c.cote = 12
    print(c.surface )
    print(50*'-')
    ce = Cercle(10)
    print(ce.surface)
    print(50*'-')
    
    a = 2
    print(a)   
    print(type(a))   
    print(type(int))
    
    
if __name__=='__main__':
    main()
