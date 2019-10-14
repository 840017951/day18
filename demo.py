import time
import threading


def sing():
    for i in range(5):
        print("千里香---%d" %i)
        time.sleep(1)
        

def dance():
    for i in range(5):
        print("鬼步舞---%d" %i)
        time.sleep(1)

        
def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    
    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        
        if len(threading.enumerate()) == 1:
            break
    



if __name__ == "__main__":
    main()
