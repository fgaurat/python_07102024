import sys

def main():
    a=2
    b=2
    print(a,hex(id(a)))
    print(b,hex(id(b)))
    # a=3
    # print(a,hex(id(a)))
    
    c = 59875615878
    print(sys.getrefcount(59875615878))
    d = 59875615878
    print(sys.getrefcount(59875615878))
if __name__=='__main__':
    main()
