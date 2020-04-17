import socket

def append_header(msg):
    '''
    Takes string msg, and appends 10 character.
    '''
    # State variables
    header_length = 10
    msg_len = len(msg)

    # Create message header without padding
    msg_header = str(msg_len)

    # Check to make sure our string (ex. '34') is not longer than max header size
    if(len(msg_header)>header_length):
        print('ERROR: message too long!')
        return 1

    padding_len = header_length - len(msg_header)
    padding = ' ' * padding_len

    # HEADER without time
    msg_header = msg_header + padding
    msg_with_header = msg_header + msg

    # HEADER with time
    # msg_header = msg_header + padding
    # msg_header_with_time = msg_header + time.asctime()
    # msg_with_header = msg_header_with_time + msg

    return msg_with_header

def main():
    # We are binding to no IP, because we want to listen from all directions
    PORT = 1281
    IP_to_connect = ""

    # Create socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Bind to IP and Port
    s.bind((IP_to_connect,PORT))
    # Begin listening on Channel
    s.listen(5)

    # Message to send client (play around with different length messages etc.)
    msg = "this is a wonderful message that you would like to hear!"
    message_with_header = append_header(msg)

    while True:
        # The script will wait at this line until someone tries to connect with us.
        # Once some does, with get a new socket clientsocket that is associated with them, and a
        # address, which is thier IP.
        clientsocket, address = s.accept()
        print("Connection with " + str(address) + " has been established!")
        
        # Lets send them pur welcome message!!
        clientsocket.send(message_with_header)



if __name__ == '__main__':
    main()