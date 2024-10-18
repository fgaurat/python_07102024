import requests
from bs4 import BeautifulSoup
import time

def main():
    start = time.perf_counter()
    
    url ="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    # all_a = soup.find_all('a')
    # for a in all_a:
    #     print(a['href'])
    
    all_a = [a['href'].strip() for a in soup.find_all('a') if a['href'].endswith(".log")]
    for a in all_a:
        file_link = f"{url}{a}"
        print(file_link)
        response = requests.get(file_link)
        with open(a,"w") as f:
            f.write(response.text)
        
    end = time.perf_counter()
    print(f"time {end-start:.2}s")




if __name__=='__main__':
    main()
