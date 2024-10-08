
def main():
    a=2
    l =[]
    for i in range(10,70,10):
        l.append(i) 
    
    l = list(map(lambda i:i,range(10,70,10)))
    print(l)
    
    l = [i for i in range(10,70,10)]
    print(l)
    
if __name__=='__main__':
    main()
