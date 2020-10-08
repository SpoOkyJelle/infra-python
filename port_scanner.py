import socket
import time
import threading
import optparse

import scapy.all as scapy
from scapy.layers.inet import IP, ICMP


from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()


def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="target IP/ IP range")
    args_options, arguments = parser.parse_args()
    return args_options


options = getArguments()

t_IP = socket.gethostbyname(options.target)
print ('Starting scan on host: ', t_IP)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done() 
      
q = Queue()

# start counter to see how long scan takes
startTime = time.time()
   
for x in range(100):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
   
for worker in range(1, 500):
    q.put(worker)
   
q.join()
print('Time taken:', time.time() - startTime)