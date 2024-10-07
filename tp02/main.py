def log(log_filename):
    def decorator(func):
        
        def wrapper(*args,**kwargs):
            print(f'LOGS to {log_filename}',*args,**kwargs)
            r = func(*args,**kwargs)
            print(f'LOGS to {log_filename} RETURN',r)
            return r
        return wrapper
    return decorator


@log('the_log.log')
def hello(name,firstName):
    
    h = f"hello {name} {firstName}"
    return h

def main():
    r = hello('GAURAT','Fred')
    print(r)
    
    
if __name__=='__main__':
    main()
