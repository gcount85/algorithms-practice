import multiprocessing
import time

lock = multiprocessing.Lock()


def print_numbers():
    for i in range(10):
        # time.sleep(1)  # 1초 마다 숫자를 출력한다
        with lock:
            print(i)


def print_letters():
    for letter in '가나다라마바사아자차':
        # time.sleep(1)  # 1초 마다 문자를 출력한다
        with lock:
            print(letter)


# 프로세스를 생성하는 작업은 메인 코드 블럭에 넣어야 한다
if __name__ == '__main__':

    # 두 개의 프로세스를 만든다
    # print_numbers를 호출하는 프로세스
    p1 = multiprocessing.Process(target=print_numbers)
    # print_letters를 호출하는 프로세스
    p2 = multiprocessing.Process(target=print_letters)

    # 프로세스를 시작시킨다
    p1.start()
    p2.start()

    # 두 프로세스가 끝날 때까지 기다린다
    p1.join()
    p2.join()

    print("Done!")


# 스레드의 경우보다는 규칙적으로 p1 -> p2 순으로 번갈아가며 출력 작업을 실시한다 (완벽하진 않음!)
