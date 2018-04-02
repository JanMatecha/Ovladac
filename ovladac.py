import ads1x15
from machine import I2C, Pin
from oled import *
import socket  # for sockets
import sys  # for exit

oled = Oled()
oled.head()
oled.square()

i2c = I2C(scl=Pin(5), sda=Pin(4))
ads = ads1x15.ADS1015(i2c=i2c)




try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()

print('Socket Created')

#host = '127.0.0.1'
host = '10.0.0.10'
#host = '10.0.0.2'
port = 8888


# Connect to remote server
s.connect((host, port))


print('Socket Connected to ' + host )



while True:
    y = ads.read(0)
    x = ads.read(1)
    print(x,y)
    x_new = int(x/42)+44
    y_new = int(y/42)+12
    print(x_new, y_new)
    oled.show_position(x_new, y_new)

# Send some data to remote server



    message = "konec"
    if y > 790:
        message = "MF:" + str(int((y-790)/10))
    if y < 790:
        message = "MB:" + str(int((790-y)/10))


    try:
        # Set the whole string
        s.sendall(message.encode('utf-8'))
    except socket.error:
        # Send failed
        print('Send failed')
        sys.exit()

    print('Message send successfully')

    # Now receive data
    reply = s.recv(1024)

    print(reply.decode('ascii'))

s.close()