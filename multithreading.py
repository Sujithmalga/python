import threading
import time

def squaring(num):
    print(f'{num*num}')
    
def cubing(num):
    print(f'{num*num*num}')

if __name__ =='__main__':
    x = threading.Thread(target=squaring,args=(12,))
    time.sleep(20)
    y  = threading.Thread(target=squaring, args=(21,))
    x.start()
    y.start()  
    x.join()
    y.join()
    