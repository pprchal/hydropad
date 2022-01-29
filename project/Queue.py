from threading import Condition

class Queue():
    queue = []
    cond = Condition()

    @classmethod 
    def queue_message(cls, msg):
        print(msg)
        cls.queue.append(msg)
        cls.cond.notify()

    
