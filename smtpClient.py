from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):

    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')
    else:
        print('220 reply received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    else:
        print('250 reply received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCmd = 'MAIL FROM:<sender@example.com>\r\n'
    clientSocket.send(mailFromCmd.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(f"MAIL FROM Response: {recv2}")
    if recv2[:3] != '250':
        print('250 reply not received from server for MAIL FROM.')
    else:
        print('250 reply received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCmd = 'RCPT TO:<recipient@example.com>\r\n'
    clientSocket.send(rcptToCmd.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(f"RCPT TO Response: {recv3}")
    if recv3[:3] != '250':
        print('250 reply not received from server for RCPT TO.')
    else:
        print('250 reply received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    if recv_data[:3] != '354':
        print('354 reply not received from server for DATA.')
    else:
        print('354 reply received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    message = "Subject: SMTP Python Test \r\n\r\nThis is the body of my email for my Python server assignment \r\n"
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    endmsg = "\r\n.\r\n"
    clientSocket.send((message + endmsg).encode())
    recv_message = clientSocket.recv(1024).decode()
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    if recv_data[:3] != '250':
        print('250 reply not received from server for DATA.')
    else:
        print('250 reply received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv_quit = clientSocket.recv(1024).decode()
    print(recv_quit)
    if recv_quit[:3] != '221':
        print('221 reply not received from server for QUIT.')
    else:
        print('Session terminated gracefully.')
    # Fill in end



if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
