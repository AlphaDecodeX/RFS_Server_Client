# RFS_Server_Client

### Sending Commands Structure:- 
- All commands are implemented in lower case. Internally, in python commands are converted in lowercase only

### 1. ls command structure:- 

<img width="741" alt="image" src="https://user-images.githubusercontent.com/91979252/190846195-ac6c7df8-7b6a-40ca-a271-27c4e6259dd5.png">

### 2. cwd command is implemented simply using OS system call getcwd() and been sent to the client.

Here is the working of both cwd and ls commands:-
#### ls Command:-
![image](https://user-images.githubusercontent.com/91979252/190846308-b9276414-f850-4744-82da-ae097a91666c.png)
#### cwd Command:-
![image](https://user-images.githubusercontent.com/91979252/190846321-652d3dfe-6809-4d7c-939f-dd5ea0dec7ca.png)

### 3. Talking about cd command, It is not a single command it contains two things first one is cd and second is <dirName>. cd <dir_name>

```
  We can see the commands having more than one thing like here in cd command, we did appened them both using "_" so on the server side we'll recieve "cd_Desktop" if we want to switch our current directory to Desktop.
```

Here, is the working:-
![image](https://user-images.githubusercontent.com/91979252/190846341-8bb0115c-ea97-48ad-857b-586fc622c41d.png)

- You can see we used cd ../ command here to see if we can switch one directory back or not.

### 3. Working of Download and Upload File from server to client [DWD] and client to server [UPD] :-

- Note: It has been explained through the video for better understanding:-

https://drive.google.com/file/d/1lKVBWgPcsAzOBzz5FRO4gkNdaPJRelq8/view?usp=sharing


- Note:-

ls, cd, cwd commands are implemented completely. DWD and UPD are implemented without encryption and decryption.
