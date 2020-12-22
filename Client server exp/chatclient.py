import socket
import select
import errno

# Existing Users
name1 = "Tom"
name2 = "David"
name3 = "Beth"

# Network info
PORT = 13386
IP = "127.0.0.1"
HEADER_SIZE = 10

# Option for log in function
choice = input("Enter any key to log in, or enter a 1 create a new account: ")
if choice == "1":
	# User chooses new username
	newuser = input("Enter your new username: ")
	while len(newuser) > 32 or newuser == "Tom" or newuser == "David" or newuser == "Beth":
		newuser = input("Username is unavailable. Enter your new username: ")
	# User chooses new password
	newpassword = input("Enter your new password: ")
	while len(newpassword) < 4 or len(newpassword) > 8:
		newpassword = input("Password is invalid. Enter a new password between 4 to 8 characters: ")
		
# Login validation
check = 0
while check == 0:
	my_username = input("Username: ")
	
	if my_username == name1:
		check = 1
	elif my_username == name2:
		check = 2
	elif my_username == name3:
		check = 3
	elif choice == "1" and my_username == newuser:
			check = 4
	else:
		check = 0
		
 
# Initialize the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Make connection to network
client_socket.connect((IP, PORT))
 
# Ensure connection cannot be blocked
client_socket.setblocking(False)
 
# Convert input username and password for parsing for server
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_SIZE}}".encode('utf-8')
client_socket.send(username_header + username)

# Existing passwords
pw1 = "Tom11"
pw2 = "David22"
pw3 = "Beth33"

# Validation for password credentials
checkB = 0
while checkB == 0:
	
	my_password = input("Password: ")
	
	if my_username == 'placeholder':
			checkB = -1
	elif check == 1 and my_password == pw1:
		checkB = 1
	elif check == 2 and my_password == pw2:
		checkB = 2
	elif check == 3 and my_password == pw3:
		checkB = 3
	elif choice == "1":
		if check == 4 and my_password == newpassword:
			checkB = 4
	else:
		checkB = 0

# Live chatroom communication for logged in user activity
while True:
 	
	# User enters credential for validation by login function
	message = input(f'{my_username} > ')
		
 
	# Send messages to the server
	if message:
 
		# Convert message for parsing by the server to appropriately display it
		message = message.encode('utf-8')
		header_msg = f"{len(message):<{HEADER_SIZE}}".encode('utf-8')
		client_socket.send(header_msg + message)
 
	try:
		# Display messages to server side output
		while True:
 
			username_header = client_socket.recv(HEADER_SIZE)
 
			# Handle a closed connection from server
			if not len(username_header):
				print('Closed connection from server')
				sys.exit()
			username_length = int(username_header.decode('utf-8').strip())
			username = client_socket.recv(username_length).decode('utf-8')
			header_msg = client_socket.recv(HEADER_SIZE)
			message_length = int(header_msg.decode('utf-8').strip())
			message = client_socket.recv(message_length).decode('utf-8')
 
			# Display message to server output from user
			print(f'{username} -> {message}')
 
	# Handle absense of incoming data or errorenous data
	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Exiting due to error in reading data: {}'.format(str(e)))
			sys.exit()
 
		continue
		
 	# Exit if there is error from reading data 
	except Exception as e:
		print('Exiting due to error in reading data: '.format(str(e)))
		sys.exit()