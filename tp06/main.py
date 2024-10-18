from RectangleSingleton import RectangleSingleton
from RectangleMetaSingleton import RectangleMetaSingleton
def main():
    r = RectangleSingleton()
    r1 = RectangleSingleton()
    r2 = RectangleMetaSingleton()
    r3 = RectangleMetaSingleton()
    print(hex(id(r)))
    print(hex(id(r1)))
    print(50*'-')
    a = 2
    print( type(a))
    print( type(int))
    
    print(hex(id(r2)))
    print(hex(id(r3))) 
    
if __name__=='__main__':
    main()
