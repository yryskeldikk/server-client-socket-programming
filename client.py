from socket import*
import time

SENDING_COOLDOWN = 0.1

BUFFER_SIZE = 4096
filename = ''
line_buffer = []

port = 16000
client = socket(AF_INET, SOCK_STREAM)
connected = False #boolean variable to check if the connection is established or not
while not connected:
    try: #connection establishment
        serverName = input("Please input the server name('localhost' for the localhost): ")
        client.connect((serverName, port))
        connected = True
        print("Connection Status: CONNECTED")
        print("IP Address:", serverName, "     ", "Port Number:", port)
    except Exception:
        print("Connection Status: CONNECTION FAILED")

while True:
    try:
        command_str = input("Please type your command (UPLOAD/DOWNLOAD/RETRIEVE filename): ") #getting user's command
        command_pieces = command_str.split() #split into command and filename
        command = command_pieces[0]

        if command in ['UPLOAD', 'DOWNLOAD']:
            client.send(command_str.encode('utf-8')); time.sleep(SENDING_COOLDOWN)
            status = client.recv(BUFFER_SIZE).decode('utf-8')
            print("IP Address:", serverName, "     ", "Port Number:", port) #IP address and port number
            print("Server:", status) #SUCCESS/ERROR
            if (status == 'SUCCESS'):
                filename = command_pieces[1]
                if command == 'UPLOAD':  #UPLOAD command
                    f = open(filename, 'r')
                    content = f.readlines()
                    for line in content:
                        client.send(line.encode('utf-8')); time.sleep(SENDING_COOLDOWN) #sending line by line
                        print('Sending line:', line.rstrip())
                        ack = client.recv(BUFFER_SIZE).decode('utf-8') #getting ack from the server
                        print('Receive ACK for line: {}'.format(line.rstrip()))

                    client.send('#\n'.encode('utf-8')); time.sleep(SENDING_COOLDOWN)#sending EOF to let the server know that it is the last line
                    print('Sending EOF')
                    ack = client.recv(BUFFER_SIZE).decode('utf-8') #getting EOF ack
                    print('Receive ACK for EOF')

                elif (command == 'DOWNLOAD'): #DOWNLOAD command
                    line = client.recv(BUFFER_SIZE).decode('utf-8') #getting first line of downloading file
                    while (line != '#'):
                        print('Line received:', line.rstrip())
                        line_buffer.append(line) #saving line in the line_buffer
                        client.send('ACK'.encode('utf-8')); time.sleep(SENDING_COOLDOWN) #sending ack to the server 
                        print('Sending ACK')
                        line = client.recv(BUFFER_SIZE).decode('utf-8') #getting next line of the file from the server

                    print('EOF received:', line.rstrip())
                    f = open(filename, 'w')
                    f.writelines(line_buffer) #creating the file and saving all the data in the line_buffer into that file
                    print('Saving to {}'.format(filename))
                    client.send('ACK'.encode('utf-8')); time.sleep(SENDING_COOLDOWN) #sendng ack
                    print('Sending ACK')
                    f.close()
                    line_buffer = []
        elif command == 'RETRIEVE': #RETRIEVE command
            client.send(command_str.encode('utf-8')); time.sleep(SENDING_COOLDOWN)
            response = client.recv(BUFFER_SIZE).decode('utf-8') #YES/NO from the server
            print("IP Address:", serverName, "     ", "Port Number:", port)
            print("Server:", response)

        elif command == 'exit': #exit command
            client.send(command_str.encode('utf-8')); time.sleep(SENDING_COOLDOWN)
            response = client.recv(BUFFER_SIZE).decode('utf-8') #getting the server response
            print("IP Address:", serverName, "     ", "Port Number:", port)
            print("Server:", response)
            client.close() #closing the TCP connection
            break

        else: #if unknown command
            client.send(command_str.encode('utf-8')); time.sleep(SENDING_COOLDOWN) #sending the server unknown command
            status = client.recv(BUFFER_SIZE).decode('utf-8') #getting server's response
            print("IP Address:", serverName, "     ", "Port Number:", port)
            print("Server:", status)
            
    except Exception:
        print("There was an error while connecting the server. Please restart the server and try again.")
        client.close()
        break