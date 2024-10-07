import copy


def main():
    l = [10,20,30,40,50]
    print(l)
    l[0]= 1000
    print(l)
    print(l[len(l)-1])
    print(l[-1])
    print(l[-4])
    print(l[2:3])# [2:3[
    print(l[2:4])# [2:4[
    print(l[2:-1])# [2:4[
    print(l[2:])
    print(l[:4])
    print(l[:])
    
    print("-"*50)
    l = [10,20,30,40,50]
    print(l)
    l1=l[:]  # shallow copy
    l1=l.copy() # shallow copy
    l1=copy.copy(l) # shallow copy
    l[0]=1000
    print(l)#[1000,20,30,40,50]
    print(l1)
    print("-"*50)
    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]
    print(l)
    l1=copy.deepcopy(l)
    l[1][1] = 1000
    print(l)
    print(l1)
    
    
    
if __name__=='__main__':
    main()
