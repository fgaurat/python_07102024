import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp

async def download(url,log_file):
    file_link = f"{url}{log_file}"
    response = requests.get(file_link)
    with open(log_file,"w") as f:
        f.write(response.text)

async def download_aiohttp(url,log_file):
    file_link = f"{url}{log_file}"

    async with aiohttp.ClientSession() as session:
        async with session.get(file_link) as response:

            with open(log_file,"w") as f:
                f.write(await response.text())
    
    
async def main():
    start = time.perf_counter()
    
    url ="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a = [a['href'].strip() for a in soup.find_all('a') if a['href'].endswith(".log")]
    tasks = []
    for a in all_a:
        c = download_aiohttp(url,a)
        tasks.append(c)
    
    await asyncio.gather(*tasks)
    
    end = time.perf_counter()
    print(f"time {end-start:.2}s")




if __name__=='__main__':
   asyncio.run( main())
