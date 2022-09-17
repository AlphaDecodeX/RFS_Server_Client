
import socket            
import os

s = socket.socket()        
print ("Socket successfully created")
 

port = 8080          
 
s.bind(('', port))        
print ("socket binded to %s" %(port))
 

s.listen(1)    
print ("socket is listening")           
c, addr = s.accept()
      
print ('Got connection from', addr )

def handle_command(cmd):
    if cmd == 'cwd':
        c.send(os.getcwd().encode())
        return
    elif cmd == 'ls':
        c.send("*---*".join(os.listdir()).encode())
        return
    elif '_' in cmd and cmd.split('_')[0] == 'cd':
        os.chdir(cmd.split('_')[1])
        if(cmd.split('_')[1] in os.listdir() or cmd.split('_')[1] == "../"):
            c.send("OK".encode())
        else:
            c.send("NOK".encode())
        return
    elif '_' in cmd and cmd.split('_')[0] == 'dwd':
        file = cmd.split('_')[1]
        if file not in os.listdir():
            print("NOK")
            return
        file = open(file, 'rb')
        sendData = file.read(1024)
        while sendData:
            c.send(sendData)
            sendData = file.read(1024)
        file.close()
        return
    elif '_' in cmd and cmd.split('_')[0] == 'upd':
        filename = cmd.split('_')[1]
        c.send("1".encode())
        
        file = open(filename, 'wb')
        recvData = c.recv(1)
        if("0" in recvData.decode()):
            print("NOK")
            return
        while recvData:
            file.write(recvData)
            recvData = c.recv(1024)
        
        print("OK")
        file.close()
        return

while True:
    data = c.recv(1024).decode()
    if not data:
        break
    print("From connected user: " + str(data))
    handle_command(data);

c.close()