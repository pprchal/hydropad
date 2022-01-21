import queue

class Queue():
    queue = []

    @classmethod 
    def queue_message(cls, msg):
        print(msg)
        cls.queue.append(msg)
    
