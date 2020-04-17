import socket
import time

# This is the main function and is the first function to start at run time
def main():
    # State Variables
    PORT = 1281
    IP_to_connect = socket.gethostname()

    # Create Socket, dont worry about the parametres
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Connect to socket
    s.connect((IP_to_connect,PORT))

    # Now lets recieve a message
    chars_to_recieve = 10
    msg = s.recv(chars_to_recieve)

    # Display message
    print(msg)

    l = int(msg)
    msg = s.recv(l)
    print(msg)

    # Close the socket when your program has finished
    s.close()



# Can ignore, if interested, this checks to see if this file was called directly 
# or if it included from another file (to use some of its functions)
if __name__== '__main__':
    main()
