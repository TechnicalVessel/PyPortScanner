import socket
from threading import Thread

#Main Scanning method
def scan(host, port, lst):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        if s.connect_ex((host, port))==0:
             lst.append(port)
    return

#Super Long Setup before the Scanning method
common=[80, 443, 20, 21, 22, 23, 25, 53]

customlist=[]
openlist=[]
threads=[]

input("Port Scanner (Enter to continue)")

host = input("Enter a host address: ").lstrip("https://").rstrip("/")

if int(input('''1: Scan for commonly used ports 
2. Scan for custom ports
'''))==2:
    while True:
         x=int(input("Enter a Port (Enter -1 to finish)"))
         if x==-1:
              break
         else:
              customlist.append(x)
    
    print("Scanning...")
    
    for i in customlist:
         t=Thread(target=scan, args=(host,i,openlist))
         t.start()
         threads.append(t)
    
    for i in threads:
         i.join()
else:
    print("Scanning...")
    for i in common:
        t=Thread(target=scan, args=(host,i,openlist))
        
        t.start()
        
        threads.append(t)
    for i in threads:
         i.join()
    
print("Open Ports:", openlist)

input("Press Enter to Exit...")