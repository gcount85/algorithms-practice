import multiprocessing
import time


def count_up_to(n):
    count = 0
    for i in range(n):
        count += 1
        # print(i)


def run_example():
    start_time = time.time()

    n = 100_000_000
    # n = 20000
    num_process = 2  # count 작업의 경우 프로세스가 많을 수록 빠르다(한계는 있다)

    processes = [multiprocessing.Process(target=count_up_to, args=(
        n // num_process,)) for _ in range(num_process)]

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    end_time = time.time()
    print(f"걸린 시간: {end_time - start_time: .2f} seconds")
    # count 작업의 경우 멀티 프로세싱이 훨씬 빠르다!


if __name__ == "__main__":
    run_example()
