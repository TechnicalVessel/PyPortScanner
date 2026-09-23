import socket

def scan(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        return s.connect_ex((host, port))==0

common=[80, 443, 20, 21, 22, 23, 25, 53]
customlist=[]
openlist=[]
input("Port Scanner (Enter to continue)")
host = input("Enter a host address: ")
if int(input('''1: Scan for commonly used ports
2. Scan for custom ports '''))==2:
    while True:
         x=int(input("Enter a Port (Enter -1 to finish)"))
         if x==-1:
              break
         else:
              customlist.append(x)
    print("Scanning... (This will take a while!)")
    for i in customlist:
         if scan(host,i):
              openlist.append(i)
else:
    print("Scanning... (This will take a while!)")
    for i in common:
            if scan(host, i):
                openlist.append(i)
print("Open Ports:", openlist)