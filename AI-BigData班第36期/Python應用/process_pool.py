import multiprocessing as mp
import time,os
def longTime(i):
    print('task:{}'.format(i))
    time.sleep(5)
    result=10**30
    print('result:{}'.format(result))
    return result

if __name__ == '__main__':
    start_time = time.time()
    print('母程序PID: {}'.format(os.getpid()))

    p=mp.Pool(4)
    data=p.map(longTime,iterable=range(0,4))
    p.close()
    p.join()
    print(data)

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))
