
def parse_privmsg(string_):
    msgtype = 'system'
    chatname = ''
    chatcont = ''
    string_.strip('\r\n')
    if string_.find('PRIVMSG') != -1:
        msgtype = 'message'
        chatname = string_[1:string_.find('!')]
        chatcont = string_[string_.rfind(':') + 1:]
    return msgtype, chatname, chatcont

