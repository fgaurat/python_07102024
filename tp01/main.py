def main():
    l = [10,20,30,40,50]
    to_find = 300
    for v in l:
        print(v)
        if v == to_find:
            break
    else:
        print("pas trouvé")
        
if __name__=='__main__':
    main()
