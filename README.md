# Server - Client Remote File Storage System

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










