import lib as l
# HelloWorld => PascalCase UpperCamelCase
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => kebab-case

c = "Une valeur"

def main():
    global c
    c = "Une autre valeur"
    print("dans le main",c)
    # b
    a=2
    print(a)
    print("main module",__name__)
    l.hello()
    if False:
        b=3
    # print(b)
    # print("password",lib.password)
if __name__=='__main__':
    print("avant",c)
    main()
    print("après",c)

