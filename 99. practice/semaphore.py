import threading
import time


class Semaphore:
    def __init__(self, value):
        self.value = value
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def acquire(self):  # 세마포어 값이 0이 아닐 때까지 기다렸다가 획득
        with self.lock:
            while self.value == 0:
                self.condition.wait()
            self.value -= 1

    def release(self):  # 세마포어 값을 1 증기시키고 세마포어 해제
        with self.lock:
            self.value += 1
            # self.condition.notify() # 세마포어를 기다리는 하나(혹은 n개)의 스레드 깨움
            self.condition.notify_all()  # 모든 스레드를 깨움


def worker(semaphore: Semaphore, worker_id: int):
    for _ in range(3):  # 세 번씩 일 하게 한다
        semaphore.acquire()  # 세마포어를 획득해야 일하고
        print(f"스레드 {worker_id+1} 일하는 중입니다")
        time.sleep(1)
        print(f"스레드 {worker_id+1} 일을 다 마쳤습니다!")
        semaphore.release()  # 일을 마치면 세마포어 해제
        time.sleep(2)


if __name__ == '__main__':
    num_worker = 5
    num_resource = 1  # 리소스 개수를 조절하며 테스트 해보자!

    semaphore = Semaphore(num_resource)  # 접근 가능한 리소스의 숫자만큼의 값을 가진 세마포어 생성
    threads: list[threading.Thread] = []

    for i in range(num_worker):
        t = threading.Thread(target=worker, args=(semaphore, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("세마포어 테스트 종료")
