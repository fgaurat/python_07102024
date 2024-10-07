def main():
    a = 2
    b = 3
    c = a/b
    s = f"{a=} {b=} {a/b=:.2%}"
    print(s)
    
    l = [10,20,30,40,50]

    
    s1 = "b={1}, a={0} ".format(*l)
    print(s1)
    s2 = "Bonjour {name}, {firstname}".format(name="GAURAT",firstname="Fred")
    print(s2)
    d = {"name":"GAURAT","firstname":"Fred"}
    s2 = "Bonjour {name}, {firstname}".format(**d)
    print(s2)
    p = r"c:\new_project\the_project_01"
    print(p)
if __name__ == '__main__':
    main()
