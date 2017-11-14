import threading
from queue import Queue
import time

print_lock = threading.Lock()

q = Queue()
def examplejob(worker):                             #this is a basic funtion
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, worker)

for worker in range(20):        #these are the workes or the args given to the funtion each time the funtion is called
    q.put(worker)

def threader():                 #invoking the funtion using the threader
    while True:
        worker = q.get()
        examplejob(worker)
        q.task_done()

for x in range(10):     #have 10 threads
    t = threading.Thread(target= threader)
    t.daemon = True             #the thread dies when the main thread dies
    t.start()

start = time.time()

q.join()        #the program will go beyond this line if all the taskes are over
                #i.e. the queue becomes empty

print('entire job took',time.time() - start)            #when all the taskes are exicuted then it reaches this point
