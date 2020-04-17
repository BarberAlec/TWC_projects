import numpy as np

def create_mask(bit_arr, threshold):
    # Can ignore this
    noisy_arr = (bit_arr > threshold).astype(int)

    # Convert our array to a proper binary number (can ignore)
    out = 0
    for bit in noisy_arr:
        out = (out << 1) | bit
    return out

def noisy_channel(msg,noise_var=0.25):
    ''' Uncomment print statements if you want to see what is happening :)
    I would suggest only uncommenting one at a time'''
    # for each letter(ltr) in msg, get ascii value
    ascii_list = [ord(ltr) for ltr in msg]
    #print("ascii_list: " + str(ascii_list))


    noisy_string = ""
    # For each characher in our ascii list, apply Gaussian noise
    # In other words we will randomly flip some of the bits in the ascii characters
    for ascii_char in ascii_list:
        # Create 7 noisy values (zero mean and variance of noise_var)
        noise = np.random.normal(0,noise_var,7)
        # Create mask with our noise, any 1s in the mask will flip the corresponding bit in the character
        noise_mask = create_mask(noise,0.5)
        # Apply mask and flip the bits, then convert back from ascii value to a python char
        noisy_string = noisy_string + chr(ascii_char^noise_mask)

        #print("noise: " + str(noise))
        #print("noise_mask: " + str(format(noise_mask, 'b')))
    
    return noisy_string


# START HERE

# This is your message that is being transmitted across a noisy channel
test_string = 'This is a great test message'
print("Sending message:\t" + test_string)

# Let us send it across a really noisy channel where some bits will be flipped
# noise_var measures how noisy the channel is
# What happens when the noise is Very large? What is the worst possible likilihood of a bit flipping?
out_str = noisy_channel(test_string,noise_var=0.24)

# Print corrupted message
print("Noisy message recieved:\t" + out_str)

# TASK:
#       > Can you do anything to imporve the quality of recieved message and make it less noisy?
#       > Try implement in code, but more importantly try answer the problem in words, what are
#           the draw-backs of your approach?
#       > Every group must talk about how they would go about solving this problem to the class
#       > Try and be really creative!!!
# HINT:
#       > Brainstorm different approachs before starting to code anything!!
#       > Try recieving the same message a few times?
#       > Is there anything you can do to the message you send ?

'''
String manipulation hints

my_str = 'Hello_world'
my_str[0]  --> 'H'
my_str[-1] --> 'o'
my_str[3:9] --> 'lo wor'



For loop hints:

for i in range(10):
    print(i)
{this will print 0 to 9}

my_str = 'WORLD'
for i in range(len(my_str)):
    print(my_str[0:i])
{will print}
''
'W'
'WO'
'WOR'
'WORL'
'WORLD'
'''
