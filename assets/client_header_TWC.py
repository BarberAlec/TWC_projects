import socket
import time

# This is the main function and is the first function to start at run time
def main():
    # State Variables
    PORT = 1282
    IP_to_connect = socket.gethostname()

    # Create Socket, dont worry about the parametres
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Connect to socket
    s.connect((IP_to_connect,PORT))

    # Now lets recieve a message (You will need to change some code from
    # here down :) )
    # HINT: try recieving characters in two bursts.
    chars_to_recieve = 20
    msg = s.recv(chars_to_recieve)


    # Display message
    print(msg)

    # Close the socket when your program has finished
    s.close()



# Can ignore, if interested, this checks to see if this file was called directly 
# or if it included from another file (to use some of its functions)
if __name__== '__main__':
    main()
