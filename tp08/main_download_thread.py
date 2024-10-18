import requests
from bs4 import BeautifulSoup
import time
import threading
def download(url,log_file):
    file_link = f"{url}{log_file}"
    response = requests.get(file_link)
    with open(log_file,"w") as f:
        f.write(response.text)
    
    
    
def main():
    start = time.perf_counter()
    
    url ="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    # all_a = soup.find_all('a')
    # for a in all_a:
    #     print(a['href'])
    
    all_a = [a['href'].strip() for a in soup.find_all('a') if a['href'].endswith(".log")]
    ths = []
    for a in all_a:
        th = threading.Thread(target=download,args=(url,a))
        th.start()
        ths.append(th)
    
    [t.join() for t in ths]
    
    
    end = time.perf_counter()
    print(f"time {end-start:.2}s")




if __name__=='__main__':
    main()
