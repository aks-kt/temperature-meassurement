import sys, os
from mapping_data import hid, hid2

# Change device permission
os.system('sudo chown ktjustkt:dialout /dev/hidraw0')
# Open port with device has connected
fp = open('/dev/hidraw0', 'rb')

ss = ""
shift = False
done = False

while not done:
    # Get the character from the HID
    buffer = fp.read(8)
    for c in buffer:
        try:
            if ord(c) > 0:
                #  40 is carriage return which signifies
                #  we are done looking for characters
                if int(ord(c)) == 40:
                    done = True
                    break
                #  If we are shifted then we have to 
                #  use the hid2 characters.
                if shift:
                    # If it is a '2' then it is the shift key
                    if int(ord(c)) == 2 :
                        shift = True
                    # if not a 2 then lookup the mapping
                    else:
                        ss += hid2[ int(ord(c)) ]
                        shift = False
                #  If we are not shifted then use
                #  the hid characters
                else:
                    # If it is a '2' then it is the shift key
                    if int(ord(c)) == 2 :
                        shift = True
                    # if not a 2 then lookup the mapping
                    else:
                        ss += hid[ int(ord(c)) ]
        except TypeError:
            pass
print(ss)