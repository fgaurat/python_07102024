from RectangleSingleton import RectangleSingleton
def main():
    r = RectangleSingleton()
    r1 = RectangleSingleton()
    print(hex(id(r)))
    print(hex(id(r1)))
if __name__=='__main__':
    main()
