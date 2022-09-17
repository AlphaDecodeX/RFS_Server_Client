import socket   
import os         
 
def giveCommand():
    while True:
        cmd = str(input("Enter any command from CWD, LS, CD <dir>, DWD <file>, UPD <file> "))
        valid_cmds = ['cwd', 'ls', 'cd', 'dwd', 'upd']
        
        cmd_list = cmd.split(' ')

        if len(cmd_list)>2 or len(cmd_list)<1:
            print("Please enter a valid command")
        elif cmd_list[0].lower() not in valid_cmds:
            print("Please enter a vaild command")
        
        if cmd_list[0] in ['cwd', 'ls', 'cd']:
            data = ''
            if len(cmd_list) == 1:
                data = data+cmd_list[0].lower()
            else:
                data = data+cmd_list[0].lower()+'_'+cmd_list[1]
            s.send(data.encode())
            
            if cmd_list[0] == 'cwd':
                data = s.recv(1024).decode()
            elif cmd_list[0] == 'ls':
                data = s.recv(1024).decode().split("*---*")        
            elif cmd_list[0] == 'cd':
                data = s.recv(1024).decode()
            print("Data Recieved --> ", data)
        elif cmd_list[0] == 'dwd':
            filename = cmd_list[1]

            data = ''
            if len(cmd_list) == 1:
                print("Correct Syntax of Downloading file is :- dwd <filename>")
                continue
            else:
                data = data+cmd_list[0].lower()+'_'+cmd_list[1]
            
            s.send(data.encode())
            
            file = open(filename, 'wb')
            recvData = s.recv(1024)
            while True:
                file.write(recvData)
                recvData = s.recv(1024)


            print("OK")
            file.close()

        elif cmd_list[0] == 'upd':
            data = ''
            if len(cmd_list) == 1:
                print("Correct Syntax of Uploading file is :- upd <filename>")
                continue
            else:
                data = data+cmd_list[0].lower()+'_'+cmd_list[1]
        
            s.send(data.encode())
            recvBit = s.recv(1).decode()
            if recvBit != "1":
                continue

            filename = cmd_list[1]
            file = open(filename, 'rb')
            if filename not in os.listdir():
                s.send("0".encode())
                print("NOK")
                continue

                
            else:
                s.send("1".encode())
                sendData = file.read(1024)
                while sendData:
                    s.send(sendData)
                    sendData = file.read(1024)
            file.close()
        
            


s = socket.socket()
 
port = 8080
 
s.connect(('127.0.0.1', port))
giveCommand()

s.close()    