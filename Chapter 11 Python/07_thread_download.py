import threading
import requests
import time


def download(url):
    print(f"starting download from{url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size {len(resp.content)} bytes")

urls = [
    "https://www.pngplay.com/free-png/free"
    "https://freepngimg.com/png/24884-free-clipart"
    "https://pngimg.com/image/90777"
    

]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end - start :.2f} seconds")
