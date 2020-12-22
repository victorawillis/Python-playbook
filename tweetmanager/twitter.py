from tweet import *

def menu(list):

	user_input = int(input("Tweet Menu\n- - -\n1) Write a Tweet\n2) View Recent Tweets\n3) Search Tweets\n4) Quit\nWhat would you like to do? ")) 

	if (user_input is 1):

		name = input("What is your name? ")

		user_tweet = input("What would you like to tweet? ")

		list.append(tweet(name, user_tweet))

		print(name + " your tweet has been saved.")

	elif (user_input is 2):

		check =- 1

		if (len(list) > 4):

			check = len(list) -5

		for i in range(len(list) -1, check, -1):

			print("Author: " + list[i].get_author())
			print("Tweet: " + list[i].get_text())
			print("Time: " + list[i].get_age())

	elif(user_input is 3):

		name = input("Enter author name: ")

		for i in reversed(range(len(list))):

			if (list[i].get_author() == name):

				print("Tweet: " + str(list[i].get_text()))

				print("Time: " + str(list[i].get_age()))

	elif(user_input is 4):

		return False

	else:

		print("Please Enter valid option")

	return True

def main():

	list=[]

	loop = True

	while(loop):

		loop = menu(list)

main()
