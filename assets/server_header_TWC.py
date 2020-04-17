import socket

def append_header(msg):
    '''
    Takes string msg, and appends 10 character header.
    '''
    # Message should look like following once finished:
    # "56        this is a wonderful message that you would like to hear!"
    #  <-------->|<------------------------------------------------------>
    #   constant            Variable length of message
    #   length 10

    # Constant length portion
    header_length = 10

    # Example 56 for our case
    msg_len = len(msg)

    # Create message header without padding ("56" as string not 56 number)
    msg_header = str(msg_len)

    # Get length of number component of header (length of "56" is 2 characters)
    head_number_len = len(msg_header)

    # i.e. 10 less 2 is 8
    padding_len = header_length - head_number_len
    # padding is now 8 spaces "        "
    padding = ' ' * padding_len


    # Make header the string "56" appended with padding to make "56        "
    msg_header = msg_header + padding
    msg_with_header = msg_header + msg

    return msg_with_header

def main():
    # We are binding to no IP, because we want to listen from all directions
    PORT = 1282
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