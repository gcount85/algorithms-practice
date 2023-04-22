import threading
import requests
import time

urls = [
    'https://www.acmicpc.net/problem/1001',
    'https://www.acmicpc.net/problem/1002',
    'https://www.acmicpc.net/problem/1003',
    'https://www.acmicpc.net/problem/1004',
    'https://www.acmicpc.net/problem/1005',
]


def download_url(url):
    response = requests.get(url)
    print(f"{url}의 크기: {len(response.content)}")


# 멀티 스레딩을 사용하지 않은 경우
start_time = time.time()
for url in urls:
    download_url(url)
time_no_threading = time.time() - start_time
print(f"멀티 스레딩을 사용하지 않은 경우 걸린 시간: {time_no_threading}")  # 0.9 sec


# 멀티 스레딩을 사용한 경우
start_time = time.time()
threads = []

for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

time_w_threading = time.time() - start_time
print(f"멀티 스레딩을 사용한 경우 걸린 시간: {time_w_threading}")  # 0.2 sec로 훨씬 단축
