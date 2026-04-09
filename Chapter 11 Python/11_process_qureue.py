from multiprocessing import Process, Queue, Value

def prepare_chai(queue):
    queue.put("Masala chai is readay")



if __name__ == '__main__':
    queue =  Queue()
    p = Process(target= prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())