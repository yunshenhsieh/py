import multiprocessing as mp
import time,os
def longTime(i):
    print('task:{}'.format(i))
    time.sleep(5)
    result=10**30
    print('result:{}'.format(result))

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID: {}'.format(os.getpid()))
    w1 = mp.Process(target=longTime,args=(1,))
    w2 = mp.Process(target=longTime, args=(2,))
    w3 = mp.Process(target=longTime, args=(3,))
    w4 = mp.Process(target=longTime, args=(4,))

    w1.start()
    w2.start()
    w3.start()
    w4.start()

    w1.join()
    w2.join()
    w3.join()
    w4.join()

    end_time=time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))