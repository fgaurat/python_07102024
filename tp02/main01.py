def make_incrementor(initial_value):
    
    def the_function(value):
        return initial_value+value
    
    return the_function

def main():
    do_inc = make_incrementor(10)
    
    r = do_inc(5)
    print(r)#15
    
    r = do_inc(2)
    print(r)#12

if __name__=='__main__':
    main()
