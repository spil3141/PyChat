import threading 


thread1 = None

finished = False

def worker1():
    while(not finished):
        print("...")

thread1 = threading.Thread(target=worker1)

thread1.start()
    
input("Enter:")
finished = True

thread1.join()

print("finished")
        