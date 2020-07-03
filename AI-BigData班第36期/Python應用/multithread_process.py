import threading
import time,os
def longTime(i):
    print('task:{}'.format(i))
    time.sleep(5)
    result=10**30
    print('result:{}'.format(result))

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID: {}'.format(os.getpid()))
    processes_list=[]
    for p in range(0,4):
        a=processes_list.append(threading.Thread(target=longTime,args=(p,)))
        print(a)


    for p in range(0,4):
        processes_list[p].start()

    for p in range(0,4):
        processes_list[p].join()


    end_time=time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))