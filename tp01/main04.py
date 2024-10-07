from collections import deque

def main():
    l = [10,20,30,40,50]
    print(l)
    l.append(60)
    print(l)
    last_value = l.pop()
    print(l)
    print("last_value",last_value)
    
    # c'est moche
    # l.insert(0,-10)
    # print(l)
    # first_value = l.pop(0)
    # print(l)
    # print("first_value",first_value)
    d = deque(l)
    print(d)
    d.appendleft(-10)
    print(d)
    


if __name__=='__main__':
    main()
