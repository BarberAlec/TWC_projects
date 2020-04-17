import time

def append_header(msg):
    # Protocol variables
    header_length = 10

    msg_len = len(msg)

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
    msg = "this is a wonderful message that you would like to hear!"
    message_with_header = append_header(msg)
    print(message_with_header)


if __name__ == '__main__':
    main()