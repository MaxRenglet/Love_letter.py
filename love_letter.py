import time
import os

commande = "clear"
my_love = float("inf")

os.system(commande)

name = 'Estelle'
yes = 'yes'
good = 'good'
no = 'not good'
isplaying = True

while True:
	input_name = raw_input("What's your name ? ")


	if input_name == name:
	
		os.system(commande)
		print("Hello dear,")
		time.sleep(2)
		input_feel = raw_input("How are feel ? ")
	
		if input_feel == good:
			print("I'm glad you're feeling good !")
		
		if input_feel == no:
			print("Sorry to hear that, maybe this can cheers you up !")
		
		if input_feel != good and input_feel != no :
			print("\n\n")
			print("Sorry, I'm too stupid to understand you, please use 'good' or 'not good' as the answer.")
			time.sleep(2)
		

		time.sleep(2)
		print("I wrote a digital love letter for you ...")
		time.sleep(3)

		input_ready = raw_input("Are you ready ? ")

		if input_ready == yes:
			print("Ok, let's do this !")
			time.sleep(2)
			print("\n")
			print("Love can be screamed, can be whispered and also can be coded.")
			time.sleep(4)
			print("I can't explain how much I love you...")
			time.sleep(2)
			print("Even my computer can't put a number on that :")
			time.sleep(3)
			print("\n")
			print("my_love > 10000")
			print(my_love > 10000)
			print("\n")
			time.sleep(2)
			print("my_love > 1000000000000")
			print(my_love > 1000000000000)
			print("\n")
			time.sleep(2)
			print("my_love > 10000000000000000000000000")
			print(my_love > 10000000000000000000000000)
			print("\n")
			time.sleep(2)
			print("my_love == float('Infinity')")
			print(my_love == float("Infinity"))
			time.sleep(4)
			print("\n")
			print("That show how I feel ...")
			time.sleep(2)
			print("And show that my computer really understand me :)")
			time.sleep(3)
			print("\n")
			print("Love,")
			time.sleep(2)
			print("Max.")
			time.sleep(7)
			os.system(commande)
			print("It's now going to auto-destroy the program in :")
			time.sleep(1)
			print("3")
			time.sleep(1)
			print("2")
			time.sleep(1)
			print("1")
			time.sleep(1)
			print("goodbye")
			time.sleep(1)
			os.system(commande)
			exit()
		

		else:
			print("Tell me when you're ready to read it !")
			time.sleep(3)
			os.system(commande)

	
	
	if input_name == 'exit':
		print("	Goodbye !")
		time.sleep(1)
		os.system(commande)
		exit()
		
	else:
		print("\n\n")
		print("	Sorry, my I.A. doesn't recognize your ... You're certainly not the one.")
		print("\n")
