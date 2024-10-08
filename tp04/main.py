from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    print("cpt",Rectangle.get_cpt())
    r = Rectangle(12,6)
    print("cpt",r.get_cpt())

    # print(r.get_longueur())
    # r.set_longueur(56)
    
    print(r.longueur)
    r.longueur = 56

    print(r.surface)
  
    print(r)
    
    print(50*'-')
    r = Rectangle(12,6)
    print("cpt",Rectangle.get_cpt())

    r1 = Rectangle(12,6)
    Rectangle.cpt = 10000
    print("cpt",Rectangle.get_cpt())

    
    # if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")
    print(50*'-')
    line = "12,6"
    r = Rectangle.buildFromStr(line)
    print(r.surface)
    print(r)
    # r.toto = "truc"
    # print(r.__dict__)
    print(50*'-')
    r = DataRectangle(12,5)
    print(r.longueur)
    print(r.largeur)
    print(r)
    
    
if __name__=='__main__':
    main()
