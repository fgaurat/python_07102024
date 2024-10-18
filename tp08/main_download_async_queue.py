import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp

async def olddownload(url,log_file):
    file_link = f"{url}{log_file}"
    response = requests.get(file_link)
    with open(log_file,"w") as f:
        f.write(response.text)

 
async def olddownload_aiohttp(url,log_file):
    file_link = f"{url}{log_file}"

    async with aiohttp.ClientSession() as session:
        async with session.get(file_link) as response:

            with open(log_file,"w") as f:
                f.write(await response.text())
    

async def download(q_download,q_save):
    while True:
        url,a = await q_download.get()
        file_link = f"{url}{a}"
        async with aiohttp.ClientSession() as session:
            async with session.get(file_link) as response:
                content = await response.text()
                d = {
                    "content":content,
                    "log_file":a
                }
                q_save.put_nowait(d)
        q_download.task_done() 

async def save(q_save):
    while True:
        d = await q_save.get()
        content = d['content']
        log_file = d['log_file']
        with open(log_file,"w") as f:
            f.write(content)
        q_save.task_done() 

   
async def main():
    start = time.perf_counter()
    q_download = asyncio.Queue()
    q_save = asyncio.Queue()
    
    nb_download_workers = 10
    nb_save_workers = 10
    
    
    url ="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a = [a['href'].strip() for a in soup.find_all('a') if a['href'].endswith(".log")]
    tasks = []
    
    for i in range(nb_download_workers):
        task = asyncio.create_task(download(q_download,q_save))   
        tasks.append(task)

    for i in range(nb_save_workers):
        task = asyncio.create_task(save(q_save))  
        tasks.append(task)
    
    for a in all_a:
        t = url,a
        q_download.put_nowait(t)
    
    await q_download.join()
    await q_save.join()
    
    
    end = time.perf_counter()
    print(f"time {end-start:.2}s")

    [t.cancel() for t in tasks]



if __name__=='__main__':
   asyncio.run( main())
