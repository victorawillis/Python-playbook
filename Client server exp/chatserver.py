import socket
import select
 
# Network info
IP = "127.0.0.1"
PORT = 13386
HEADER_SIZE = 10
 
# Initiate socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
# Bind socket to connection, prepare connection for listening for connections to network server
server_socket.bind((IP, PORT))
server_socket.listen()
sockets_list = [server_socket]
 
# Obtain connected users on network
clients = {}
 
# Designate successful initiation and deployment of socket onto network
print('Chat room now live')
 
# Handles message receiving
def message_in(client_socket):
 
	try:
 
		# Store header info and handle closed connection from client
		header_msg = client_socket.recv(HEADER_SIZE)
		if not len(header_msg):
			return False

		# Convert message from transferrable data
		message_length = int(header_msg.decode('utf-8').strip())
		return {'header': header_msg, 'data': client_socket.recv(message_length)}
 
	# Unintential or unexpected client disconnect exception
	except:
		return False
 
# Receive incoming connection data from socket
while True:
	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
 
	# Index through socket connections to accept new connections
	for notified_socket in read_sockets:
		if notified_socket == server_socket:
 
			# Server will accept valid new connection and take in log in credentials
			client_socket, client_address = server_socket.accept()
			user = message_in(client_socket)
 
			# Unexpected or premature disconnect handling
			if user is False:
				continue
 
			# Successful add of new connection and correlating credentials
			sockets_list.append(client_socket)
			clients[client_socket] = user
 
			# Display successful joining of connection to the server
			print('{} has entered the chat'.format(user['data'].decode('utf-8')))
 
		# Currently connected user sendindg messages on server
		else:
			message = message_in(notified_socket)
 
			# Disconnected user, display exit message and remove their socket connectiom from the server
			if message is False:
				print('{} has left the chat'.format(clients[notified_socket]['data'].decode('utf-8')))
				sockets_list.remove(notified_socket)
				del clients[notified_socket]
 
				continue
 
			# Identify user sending message from their unique socket connection for correct message display
			user = clients[notified_socket]
			print(f'{user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
 
			# Locate correct user and send their message
			for client_socket in clients:
				if client_socket != notified_socket:
					client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
 
	# Handle unexpected socket connection errors and if occurring, remove defective user from server
	for notified_socket in exception_sockets:
		sockets_list.remove(notified_socket)
		del clients[notified_socket]