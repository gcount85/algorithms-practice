import threading
import time


def count_up_to(n):
    count = 0
    for i in range(n):
        # count += 1  # count 작업, print 작업을 비교해서 테스트
        print(i)


def run_example():
    start_time = time.time()

    # n = 100_000_000 # n의 크기를 비교하며 테스트
    n = 20000
    num_threads = 2  # 스레드 개수를 조절하며 테스트

    threads = [threading.Thread(target=count_up_to, args=(
        n // num_threads,)) for _ in range(num_threads)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"걸린 시간: {end_time - start_time: .2f} seconds")  # 2 sec


if __name__ == "__main__":
    run_example()
