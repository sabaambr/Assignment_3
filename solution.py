#Name: Saba Ambreen
#Assignment 3: Python Programming: SMTP Mail Client

from socket import *


def smtp_client(port=1025, mailServer='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailServer = 'smtp.nyu.edu'
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((mailServer, 25))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailFromCommand = 'MAIL FROM: <sabaambr@gmail.com>\r\n'
    clientSocket.send(mailFromCommand)
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command and print server response.
    rcptToCommad = 'RCPT TO: <sabaambr@gmail.com>\r\n'
    clientSocket.send(rcptToCommad)
    recv3 = clientSocket.recv(1024).decode()

    # Send DATA command and print server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(data)
    recv4 = clientSocket.recv(1024).decode()

    # Send message data.
    dataMessage = 'DATA\r\n'
    clientSocket.send(dataMessage)
    recv4 = clientSocket.recv(1024).decode()

    # Message ends with a single period.
    clientSocket.send(endmsg)
    recv5 = clientSocket.recv(1024).decode()

    # Send QUIT command and get server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand)
    recv6 = clientSocket.recv(1024).decode()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
