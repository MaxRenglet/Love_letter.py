#importer les libraire

import time
import os


#commande pour l'os (MAC)
commande = "clear"
os.system(commande)

#initialiser l'infini
my_love = float("inf")

#boolean pour les while
feel = False
ready = False

#Clefs pour y rentrer
name = 'estelle'

#compteur
compteur = 0
compteur2 = 0
compteur3 = 0

#While principale
while True:
	
	#input du nom et la suppression des capitales
	input_name = raw_input("What's your name ? ")
	input_name = input_name.lower()

	#comparaison si le nom correspond
	if input_name == name:
	
		os.system(commande)
		print("Hello dear,")
		
		#time.sleep vient de la librairie "time" et cela permet une pause dans le code de x secondes
		time.sleep(2)
		
		while feel == False:
		
			#input de feel et la suppression des capitales
			input_feel = raw_input("How are you ? [good/not good] : ")
			input_feel = input_feel.lower()
			
			if input_feel == 'good':
				feel = True
				print("	I'm glad you're feeling good !")
				
			
			if input_feel == 'not good':
				feel = True
				print("	Sorry to hear that, maybe this can cheers you up !")
				
			
			if input_feel != 'good' and input_feel != 'not good' :
			
				#compteur pour eviter de recommencer a l'infini
				compteur2=compteur2+1
				
				if compteur2 < 5:
				
					input_feel = raw_input("How are you ? [good/not good] : ")
					input_feel = input_feel.lower()
				if compteur2 == 5:
							print("\n")
							print("	Sorry, you're too stupid for that, my mistake ...")
							time.sleep(4)
							os.system(commande)
							exit()
		

		time.sleep(1)
		print("	I wrote a digital love letter for you ...")
		time.sleep(2)
		
		while ready == False:
		
			#input de ready et la suppression des capitales
			input_ready = raw_input("Are you ready ? [yes/no] : ")
			input_ready = input_ready.lower()
			if input_ready == 'yes':
				ready = True
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
				exit()
			
	
			if input_ready == 'no':
				ready = True
				print("Restart the program when you're ready to read it !")
				time.sleep(3)
				os.system(commande)
				exit()

			if input_ready != 'no' and input_ready != 'yes':
				
				compteur3=compteur3+1
							
				if compteur3 < 5:
							
					input_ready = raw_input("Are you ready ? [yes/no] : ")
					input_ready = input_ready.lower()
								
				if compteur3 == 5:
					print("\n")
					print("	Sorry, you're too stupid for that, my mistake ...")
					time.sleep(4)
					os.system(commande)
					exit()

	
	if input_name != name :
		compteur=compteur+1
		
		if compteur < 5:
			print("	Sorry, my I.A. doesn't recognize your ... You're certainly not the one.")
		
		
		if compteur == 5:
			print("\n")
			print("	Game Over, stop trying ... you're not the one !")
			time.sleep(4)
			os.system(commande)
			exit()
