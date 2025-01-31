import aiohttp
import asyncio
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlparse, urljoin

# Set the starting URL
base_url = "https://news.itmo.ru/ru/"
base_domain = urlparse(base_url).netloc
visited_urls = set()

# Async function to fetch the page content
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f'Error {response.status} on {url}')
    except Exception as e:
        print(f'Error fetching {url}: {e}')
    return None

# Async function to process a URL
async def process_url(session, url, queue, csv_writer):
    if any(x in url for x in ["en", "search", "#"]):
        return
    
    html = await fetch(session, url)
    if not html:
        return
    
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a', href=True):
        link_url = urljoin(url, link['href'])
        link_domain = urlparse(link_url).netloc
        
        if link_domain == base_domain and link_url not in visited_urls:
            visited_urls.add(link_url)
            csv_writer.writerow([link_url])
            await queue.put(link_url)

# Worker function to process URLs from queue
async def worker(session, queue, csv_writer):
    while True:
        url = await queue.get()
        await process_url(session, url, queue, csv_writer)
        queue.task_done()

# Main async function
async def main():
    queue = asyncio.Queue()
    await queue.put(base_url)
    visited_urls.add(base_url)
    
    async with aiohttp.ClientSession() as session:
        with open('links.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            workers = [asyncio.create_task(worker(session, queue, csv_writer)) for _ in range(8)]
            
            await queue.join()
            
            for w in workers:
                w.cancel()

# Run the async event loop
asyncio.run(main())
