import socket
from time import sleep
import sys

class irc_comm:
    def __init__(self, channel, nickname, token, server, port):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.channel_name = channel
        self.nickname = nickname
        self.client_token = token
        self.server_name = server
        self.server_port = port

    def send(self, msg):
        self.irc.send(("PRIVMSG " + self.channel_name + " :" + msg + "\r\n").encode('utf-8'))

    def pong(self):
        self.irc.send(("PONG :tmi.twitch.tv").encode('utf-8'))
        
    def connect(self):
        self.irc.connect((self.server_name, self.server_port))
        self.irc.send(("PASS " + self.client_token + "\r\n").encode('utf-8'))
        self.irc.send(("NICK " +  self.nickname + "\r\n").encode('utf-8'))
        self.irc.send(("JOIN #" + self.channel_name + "\r\n").encode('utf-8'))

    def disconnect(self):
        self.irc.send(("PART #" + self.channel_name + "\r\n").encode('utf-8'))
        self.irc.shutdown(socket.SHUT_RDWR)
        self.irc.close()

    def receive(self):
        text = self.irc.recv(2040)
        return text


channel_name = "einzhart"
nickname = "einzhart"
server_name  = "irc.chat.twitch.tv"
port = 6667
token = "oauth:tzkaxwnvm3si38sz8davspeijz00p6"


def main():
    irc = irc_comm(channel_name, nickname, token, server_name, port)
    irc.connect()
    while 1:
        text = irc.receive()
        if len(text):
            str1 = str(text, 'utf-8')
            print(str1)

if __name__ == '__main__':
    main()
