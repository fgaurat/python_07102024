import traceback

class DivBy12Error(Exception):
    
    def __init__(self):
        super().__init__('Division par 12 !!!!!!!!')
        

def div(a,b):
    if b == 12:
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    r=0
    try:
        print("OPEN FILE")
        r = div(a,b)
    finally:
        print("CLOSE FILE")
    return r

def main():
    try:
        a=3
        b=12 # int(input('b: '))
        c = call_div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)   
    except DivBy12Error as e:
        print("DivBy12Error",e)   
        # traceback.print_exc()     
    # except TypeError as e:
    #     print("TypeError",e)   
    #     # traceback.print_exc()     
    # except ValueError as e:
    #     print("ValueError",e)   
    #     # traceback.print_exc()     
    except Exception as e:
        print("Exception",e,type(e))   
        # traceback.print_exc()       
    else:
        print("Pas d'erreur")   

        
    print("La suite du code")
if __name__=='__main__':
    main()
