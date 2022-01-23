# server-client_remoteFileStorageSystem


# Instructions

## CLIENT

The server file client.py is written in Python 3 (suggested version >= 3.5.0). You can run the client by the following command:

   python client.py

or

   python3 client.py

Special Notes for the client:
1. When you run the client program, you can connect to the server by typing the IP address, or ‘localhost’ and pressing Enter to send it to the server. 
   If the TCP connection is failed, the error message will appear, and the program will ask you to enter the IP address again for reconnection. 
   After the TCP connection is successfully established, the program will print out the IP address, port number, connection status and ask you to enter your command. 

2. Command format: UPLOAD/DOWNLOAD/RETRIEVE filename

3. File is just a normal file with some lines. It does not end with '#\n', but instead the client program sends '#\n' individually
   to let the server know that the last line was sent. You can check 56368108-makefile.txt to test that out.

3. If you successfully entered the command, the SUCCESS status from the server will appear, and the process will start. 
   Otherwise, the ERROR message from the server will be printed out and the program will ask you to enter the command again.

4. You can exit the program by sending “exit” command to the server. 

5. If any error occurs during the process, the program will close the TCP connection and ask the user to restart the server and try again.

Development Environment: PyCharm - Windows




# Instructions

## Server

The server file *server.py* is written in Python 3 (suggested version >= 3.5.0). You can run the server by the following command:

    python server.py

or

    python3 server.py


Special Notes for the server: 

1. Generally speaking, TCP packets sent by the server should only contain one particular word or one line, e.g. "SUCCESS" or "ERROR: the file does not exist" or "xxxxxxxxxxxxxxxxx" (the first line of your downloading file). However, you might encounter a case where the packet sent by server contains the content of two or more packets, e.g. "SUCCESSxxxxxxxxxxxxxxxxx". This is because the [Nagle's algorithm](https://en.wikipedia.org/wiki/Nagle%27s_algorithm) used by Python's TCP protocol automatically combines small TCP packets that were sent in a short time. To avoid such cases, a simple solution is to let the server sleep for some time after sending each packet. That's why there is a time.sleep(SENDING_COOLDOWN) command after each send() function in the server's source code. The default SENDING_COOLDOWN value is set to 0.1 second. This value is enough when both server and client are running on the same computer. But when they were executed on two computers, letting the server sleep for 0.1 second might not be enough to solve the problem (this depends on the delay between the two computers). If you encounter such cases, you could change the default value of SENDING_COOLDOWN to a larger value, e.g. 0.5 second or 1 second. SENDING_COOLDOWN is defined at line 6 of server.py.








