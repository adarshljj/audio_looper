"""
import threading
import metr
import record
from multiprocessing import Process
# Create new threads
thread1 = metr.main()#myThread()
thread2 = record.main()#myThread()

# Start new Threads
Thread(target = metr.main).start()
Thread(target = record).start()

if __name__=='__main__':
     p1 = Process(target = metr.main())
     p1.start()
     p1.stop()
     p2 = Process(target =record.main())
     p2.start()
"""
import multiprocessing
import time
import metr
import record
def foo():
    name = multiprocessing.metr.main().name
    print ("Starting %s \n" %name)
    time.sleep(3)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = metr.main()\
                         (name='background_process',\
                          target=foo)
    background_process.daemon = True

    NO_background_process = record.main()\
                           (name='NO_background_process',\
                            target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
