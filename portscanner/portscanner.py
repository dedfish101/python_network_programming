# Multithreaded Port Scanner
# by NeuralNine Copyright (c) 2019
from queue import Queue
import socket
import threading

target = "10.10.202.42"#target ip
queue = Queue()
open_ports = []


#this function will return true if the port is open and false if the port is closed
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

#this is a feature which lets us add different types of port scanning methods 
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

#this function will list down all open ports and will append them to open port list 
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)



def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    #making threads to work upon the worker function
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join() #waits for thread until its finished

    print("Open ports are:", open_ports)

run_scanner(100, 1) #hardcoded for now but can change when needed