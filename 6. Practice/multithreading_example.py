import threading
import time


def print_numbers():
    for i in range(10):
        time.sleep(1)  # 1초 마다 숫자를 출력한다
        print(i)


def print_letters():
    for letter in '가나다라마바사아자차':
        time.sleep(1)  # 1초 마다 문자를 출력한다
        print(letter)


# 두 개의 스레드를 만든다
t1 = threading.Thread(target=print_numbers)  # print_numbers를 호출하는 스레드
t2 = threading.Thread(target=print_letters)  # print_letters를 호출하는 스레드

# 스레드를 시작시킨다
t1.start()
t2.start()

# 두 스레드가 끝날 때까지 기다린다
t1.join()
t2.join()

print("Done!")

# 두 스레드가 동시적으로 출력 작업을 실시한다
# 호출할 때마다 결과가 동일하지 않다 -> 결과 예측 X
