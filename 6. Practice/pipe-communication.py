import multiprocessing
import time


def child_process(conn):
    print("자식 프로세스 시작했다!")
    time.sleep(3)
    print("자식 프로세스 끝났다!")
    conn.send("자식 프로세스 종료되었습니다.")
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=child_process, args=(child_conn,))
    p.start()

    print("부모 프로세스가 자식 프로세스의 종료 시그널을 기다리고 있어요")
    msg = parent_conn.recv()  # msg를 받을 때까지 block 되어 기다린다
    print("부모 프로세스가 메시지 받음: ", msg)

    p.join()
    print("모든 프로세스가 종료되었습니다.")
