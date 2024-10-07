def hello(**kwargs):
    print(kwargs)
    print("hello",kwargs['name'],kwargs['firstName'])

def add(*values):
    print(values)
    r = 0
    for value in values:
        r+= value
    return r
def hello_p(name,firstName,/): # positional
    print(kwargs)
    print("hello",name,firstName)

def hello_kw(*,name,firstName): # keywords
    print(kwargs)
    print("hello",name,firstName) 
    
    
def main():
    l = [10,20,30,40,50]
    r = add(*l)# add(10,20,30,40,50)
    print(r) # 150
    
    r = add(10,20,30,40,50)
    print(r)
    print(50*'-')
    
    a,b,c,*_ = [10,20,30,40,50]
    print(a)
    print(50*'-')
    
    # hello("GAURAT","Frédéric")
    hello(firstName="Frédéric",name="GAURAT",age=48,job="dev")
    

if __name__=='__main__':
    main()
