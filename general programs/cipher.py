# cipher
ar1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i','j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
ar2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '<', '>', '?', '=', ' ']

# menu loop
while (True):
	
	print("1. Encode a message\n2. Decode a message\n3. Exit\n")
	option = input("Enter an option: ")
	
	# encode
	if option == '1':
		# empty list for new message
		a = []

		# assemble "encoded" message
		x = input("Enter a message: ")
		for i in range(len(x)):
			for j in range(len(ar1)):
				if x[i] == ar1[j]:
					a.append(ar2[j])


		# print new message
		print("Encoded message: ", end = '')
		for i in range(len(a)): 
			print(a[i], end = '')
		break
		
	# decode
	if option == '2':
		# empty list for new message
		a = []

		# assemble "decoded" message
		x = input("Enter a message: ")
		for i in range(len(x)):
			for j in range(len(ar1)):
				if x[i] == ar2[j]:
					a.append(ar1[j])


		# print new message
		print("Decoded message: ", end = '')
		for i in range(len(a)): 
			print(a[i], end = '')
		break
		
		break
		
	# exit
	if option == '3':
		print("")
		exit()
	else:
		print("Error: enter a 1, 2, or 3\n")