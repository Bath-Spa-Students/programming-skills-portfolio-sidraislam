budget = 60
USB_COST= 7
num_USB = budget/ USB_COST
num_USB = int(num_USB)
remainder = budget - (num_USB * USB_COST)
print ("numbers of usb which can be bought:", num_USB)
print ("money left:", remainder)