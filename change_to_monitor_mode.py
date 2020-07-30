import os

def change_mac_add(addr):
	os.system('ifconfig wlan0 down')
	os.system('ifconfig wlan0 hw ether {}'.format(addr))
	os.system('ifconfig wlan0 up')

def change_to_monitor_mode():
	os.system('ifconfig wlan0 down')
	os.system('airmon-ng check kill')
	os.system('iwconfig wlan0 mode monitor')
	os.system('ifconfig wlan0 up')

addr = input('Enter the Mac Address to Be changed ')
change_mac_add(addr)
change_to_monitor_mode()
print('Sucessfully changed to {}'.format(addr))

