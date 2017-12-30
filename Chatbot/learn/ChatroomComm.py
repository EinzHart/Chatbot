import socket
import sys

class chatroom:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(("PRIVMSG " + chan + " :" + msg + "\r\n").encode('utf-8'))

    def connect(self, server):
        self.irc.connect((server, 6667))
        self.irc.send("PASS oauth:tzkaxwnvm3si38sz8davspeijz00p6\r\n".encode('utf-8'))
        self.irc.send("NICK einzhart\r\n".encode('utf-8'))
        self.irc.send("JOIN #einzhart\r\n".encode('utf-8'))

    def disconnect(self):
        self.irc.send("PART #einzhart\r\n".encode('utf-8'))
        self.disconnect()

    def receive(self):
        text = self.irc.recv(2040)

        return text


channel = "einzhart"
server = "irc.chat.twitch.tv"

def main():
    irc = chatroom()
    irc.connect(server)

    while 1:
        text = irc.receive()
        if len(text):
            str1 = str(text, 'utf-8')
            print(str1)

if __name__ == '__main__':
    main()